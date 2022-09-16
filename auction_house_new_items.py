import datetime
from time import time
import time
import requests

from utils.MySQL_utils import MySQL

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
        time.sleep(0.5)

    print(len(all_auctions))
    return all_auctions

def get_new_auctions(page: int):
    return requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()


def insert_item_into_sql_if_it_is_interesting(auction):
    if is_item_interesting(auction):
        print(auction["item_name"], "coins:", auction["starting_bid"])
        MySQL.Functions.insert_active_auction_item_data(connection,
                                                        auction_id=auction["uuid"],
                                                        item_name=auction["item_name"].replace("'", "`"),
                                                        price=auction["starting_bid"],
                                                        start_time=epoch_to_datetime_from_miliseconds(auction["start"]),
                                                        end_time=epoch_to_datetime_from_miliseconds(auction["end"]))


def get_epoch_time():
    return round(time.time() * 1000 - 10000)


def is_auction_new(last_checked_auction: datetime, new_auction: datetime):
    return new_auction > last_checked_auction


def is_item_interesting(auction):
    return auction["bin"] is True and auction["starting_bid"] >= 100000


def epoch_to_datetime_from_miliseconds(epoch: int):
    return datetime.datetime.fromtimestamp(epoch/1000)


connection = MySQL.Functions.connect_to_skyblock_database()
MySQL.Functions.delete_all_active_auctions_records(connection)

time_of_last_checked_item = datetime.datetime.now()

current_auctions = get_all_active_auctions()
for auction in current_auctions:
    insert_item_into_sql_if_it_is_interesting(auction)

while True:
    current_auctions = get_new_auctions(page=0)

    if current_auctions["success"]:
        for auction in current_auctions["auctions"]:
            auction_start_date = epoch_to_datetime_from_miliseconds(auction["start"])
            if is_auction_new(time_of_last_checked_item, auction_start_date):
                insert_item_into_sql_if_it_is_interesting(auction)
            else:
                break
        time_of_last_checked_item = epoch_to_datetime_from_miliseconds(current_auctions["auctions"][0]["start"])
    time.sleep(1.5)
