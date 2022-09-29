import datetime
from time import time
import time
import requests

from utils.MySQL_utils import MySQL
from utils.auction_house_utils import AuctionHouse
from utils.quality_of_life_utils import QOL


def reset_all_active_auctions(connection):
    saved_active_auctions = MySQL.Functions.get_active_auctions_table(connection)
    saved_auctions_ids = []

    for row in saved_active_auctions:
        saved_auctions_ids.append(row.auction_id)

    total_pages: int = get_new_auctions(page=0)["totalPages"]
    for i in range(total_pages):
        print("page", i)
        current_page = get_new_auctions(page=i)
        if current_page["success"]:
            for active_auction in current_page["auctions"]:
                if active_auction["uuid"] not in saved_auctions_ids:
                    insert_item_into_sql_if_it_is_interesting(active_auction)
                    saved_auctions_ids.append(active_auction["uuid"])
        time.sleep(1)

def get_all_active_auctions():
    total_pages: int = get_new_auctions(page=0)["totalPages"]

    all_auctions = []
    used_auction_ids = []
    for i in range(total_pages):
        print("page", i)
        auction_page = get_new_auctions(page=i)
        if auction_page["success"]:
            for auction in auction_page["auctions"]:
                if auction["uuid"] not in used_auction_ids:
                    all_auctions.append(auction)
                    used_auction_ids.append(auction["uuid"])

    print(len(all_auctions))
    return all_auctions


def get_new_auctions(page: int):
    try:
        return requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()
    except:
        time.sleep(120)
        get_new_auctions(page)


def insert_item_into_sql_if_it_is_interesting(auction):
    if is_item_interesting(auction):
        print(auction["item_name"], "coins:", auction["starting_bid"])
        MySQL.Functions.insert_active_auction_item_data(
            connection,
            auction_id=auction["uuid"],
            item_name=AuctionHouse.add_suffix_to_name_based_on_item_bytes(auction["item_name"].replace("'", "`"), auction["item_bytes"]),
            price=auction["starting_bid"],
            start_time=QOL.epoch_to_datetime_from_miliseconds(auction["start"]),
            end_time=QOL.epoch_to_datetime_from_miliseconds(auction["end"]),
            extra_info=AuctionHouse.get_extra_info_from_item_bytes(auction["item_bytes"]),
            amount=AuctionHouse.get_item_count_from_item_bytes(auction["item_bytes"]))


def is_auction_new(last_checked_auction: datetime, new_auction: datetime):
    return new_auction > last_checked_auction


def is_item_interesting(auction):
    return auction["bin"] is True and auction["starting_bid"] >= 100000


connection = MySQL.Functions.connect_to_skyblock_database()
MySQL.Functions.delete_all_active_auctions_records(connection)

time_of_last_checked_item = datetime.datetime.now()
time_of_next_auction_reset = datetime.datetime.now() - datetime.timedelta(hours=2)
MySQL.Functions.delete_all_active_auctions_records(connection)
while True:
    time_right_now = datetime.datetime.now()
    print("time right now:", time_right_now)
    print("time of next check:", time_of_next_auction_reset)
    if time_right_now >= time_of_next_auction_reset:
        reset_all_active_auctions(connection)
        time_of_next_auction_reset = time_right_now + datetime.timedelta(minutes=5)

        active_auctions = MySQL.Functions.get_active_auctions_table(connection)
        auction_ids_list = []
        for auction in active_auctions:
            auction_ids_list.append(auction.auction_id)

    try:
        current_auctions = get_new_auctions(page=0)
    except:
        time.sleep(120)
        continue

    try:
        if current_auctions["success"]:
            for auction in current_auctions["auctions"]:
                auction_start_date = QOL.epoch_to_datetime_from_miliseconds(auction["start"])
                if auction["uuid"] not in auction_ids_list:
                    insert_item_into_sql_if_it_is_interesting(auction)
                    auction_ids_list.append(auction["uuid"])
    except Exception as e:
        print(e)
        print(current_auctions)
        break

    time.sleep(30)
