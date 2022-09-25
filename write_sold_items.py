import datetime
import time
from dataclasses import dataclass

import requests

from utils.MySQL_utils import MySQL
from utils.quality_of_life_utils import QOL


@dataclass
class EndedAuction:
    auction_id: str
    end_time: datetime
    price: int
    BIN: bool
    buyer: str
    seller_profile: str
    item_bytes: str


def get_interesting_recently_ended_auctions():
    auctions = get_all_recently_ended_auctions()
    auction_list = []

    for auction in auctions:
        if auction.BIN and auction.price >= 100000:
            auction_list.append(auction)

    return auction_list


def get_all_recently_ended_auctions():
    auctions = requests.get("https://api.hypixel.net/skyblock/auctions_ended").json()

    ended_auctions_list = []
    for auction in auctions["auctions"]:
        ended_auctions_list.append(EndedAuction(
            auction_id=auction["auction_id"],
            end_time=QOL.epoch_to_datetime_from_miliseconds(auction["timestamp"]),
            price=auction["price"],
            BIN=auction["bin"],
            buyer=auction["buyer"],
            seller_profile=auction["seller_profile"],
            item_bytes=auction["item_bytes"]
        ))

    return ended_auctions_list


connection = MySQL.Functions.connect_to_skyblock_database()

while True:
    print("getting new ended auctions...")
    active_auctions = MySQL.Functions.get_active_auctions_table(connection)
    print(len(active_auctions))
    ended_auctions = get_interesting_recently_ended_auctions()

    for ended_auction in ended_auctions:
        for active_auction in active_auctions:
            if ended_auction.auction_id == active_auction.auction_id:
                MySQL.Functions.insert_finished_auction_item_data(
                    connection,
                    auction_id=ended_auction.auction_id,
                    item_name=active_auction.item_name,
                    price=ended_auction.price,
                    start_time=active_auction.start_date,
                    end_time=ended_auction.end_time,
                    buyer=ended_auction.buyer,
                    seller_profile=ended_auction.seller_profile,
                    extra_info=active_auction.extra_info,
                    amount=active_auction.amount)
                print("item sold")

                MySQL.Functions.delete_finished_auction_from_active_auctions(connection, active_auction.auction_id)
    if len(active_auctions) >= 1:
        for active_auction in active_auctions:
            if active_auction.end_date < datetime.datetime.now():
                print(active_auction.end_date)
                MySQL.Functions.delete_finished_auction_from_active_auctions(connection, active_auction.auction_id)
    time.sleep(30)


