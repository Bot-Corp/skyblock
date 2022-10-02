import datetime
import os
import sys
import time

from utils.MySQL_utils import MySQL
from utils.active_auctions_utils import ActiveAuctions

connection = MySQL.Functions.connect_to_skyblock_database()
MySQL.Functions.delete_all_active_auctions_records(connection)
items_to_bid = ActiveAuctions.Functions.get_names_of_items_to_bid(connection)
items_to_bid = ActiveAuctions.Functions.touple_list_to_string_list(items_to_bid)

time_of_last_checked_item = datetime.datetime.now()
time_of_next_auction_reset = datetime.datetime.now() - datetime.timedelta(hours=2)

while True:
    time_right_now = datetime.datetime.now()
    if time_right_now >= time_of_next_auction_reset:
        ActiveAuctions.Functions.reset_all_active_auctions(connection)
        time_of_next_auction_reset = time_right_now + datetime.timedelta(minutes=20)

        active_auctions = MySQL.Functions.get_active_auctions_table(connection)
        auction_ids_list = []
        for auction in active_auctions:
            auction_ids_list.append(auction.auction_id)

    current_auctions = ActiveAuctions.Functions.get_new_auctions(page=0)
    try:
        if current_auctions["success"]:
            auctions_added = 0
            for auction in current_auctions["auctions"]:
                auction = ActiveAuctions.Functions.change_active_auction_dict_to_class(auction)
                if auction.auction_id not in auction_ids_list:

                    if ActiveAuctions.Functions.is_item_interesting(auction):
                        if auction.item_name in items_to_bid:
                            median = ActiveAuctions.Functions.get_item_median_price(connection, auction.item_name)
                            if auction.price / auction.amount <= median * 0.8 or \
                                    median - (auction.price / auction.amount) >= 10000000:
                                print(auction.item_name, "coins:", auction.price, "median:", median, "amount:", auction.amount, "stack price:", median*auction.amount)
                                print(f"/viewauction {auction.auction_id}")

                    is_inserted = ActiveAuctions.Functions.insert_item_into_sql_if_it_is_interesting(connection, auction)
                    if is_inserted:
                        auctions_added += 1
                    auction_ids_list.append(auction.auction_id)
            print("auctions added:", auctions_added)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print("ERROR", e)
        break

    time.sleep(5)
