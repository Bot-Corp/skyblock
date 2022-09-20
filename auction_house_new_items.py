import datetime
from time import time
import time
import requests

from utils.MySQL_utils import MySQL
from utils.quality_of_life_utils import QOL


def reset_all_active_auctions(connection):
    current_auctions = get_all_active_auctions()
    saved_active_auctions = MySQL.Functions.get_active_auctions_table(connection)
    saved_auctions_ids = []

    for row in saved_active_auctions:
        saved_auctions_ids.append(row.auction_id)

    for active_auction in current_auctions:
        if active_auction["uuid"] not in saved_auctions_ids:
            insert_item_into_sql_if_it_is_interesting(active_auction)


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
    try:
        return requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()
    except:
        time.sleep(120)
        get_new_auctions(page)


def insert_item_into_sql_if_it_is_interesting(auction):
    if is_item_interesting(auction):
        print(auction["item_name"], "coins:", auction["starting_bid"])
        MySQL.Functions.insert_active_auction_item_data(connection,
                                                        auction_id=auction["uuid"],
                                                        item_name=auction["item_name"].replace("'", "`"),
                                                        price=auction["starting_bid"],
                                                        start_time=QOL.epoch_to_datetime_from_miliseconds(auction["start"]),
                                                        end_time=QOL.epoch_to_datetime_from_miliseconds(auction["end"]),
                                                        item_bytes=auction["item_bytes"])


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

    try:
        current_auctions = get_new_auctions(page=0)
    except:
        time.sleep(120)
        continue
    if current_auctions["success"]:
        for auction in current_auctions["auctions"]:
            auction_start_date = QOL.epoch_to_datetime_from_miliseconds(auction["start"])
            if is_auction_new(time_of_last_checked_item, auction_start_date):
                insert_item_into_sql_if_it_is_interesting(auction)
            else:
                break
        time_of_last_checked_item = QOL.epoch_to_datetime_from_miliseconds(current_auctions["auctions"][0]["start"])

    time.sleep(2)
