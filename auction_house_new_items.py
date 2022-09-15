from time import time
import time

import mysql.connector
from mysql.connector import Error
import pandas as pd
import requests


def get_new_auctions(page: int):
    return requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()


def get_epoch_time():
    return round(time.time() * 1000 - 10000)


def is_auction_new(last_checked_auction: int, new_auction: int):
    return new_auction > last_checked_auction


def is_item_interesting(auction):
    return auction["bin"] is True and auction["starting_bid"] >= 100000


time_of_last_checked_item = get_epoch_time()
while True:
    current_auctions = get_new_auctions(page=0)

    if current_auctions["success"]:
        for auction in current_auctions["auctions"]:
            if is_auction_new(time_of_last_checked_item, auction["start"]):
                if is_item_interesting(auction):
                    print(auction["item_name"], "coins:", auction["starting_bid"])
            else:
                break
        time_of_last_checked_item = current_auctions["auctions"][0]["start"]
    time.sleep(1)
