import datetime
import time

import requests

from utils.MySQL_utils import MySQL
from utils.auction_house_utils import AuctionHouse
from utils.quality_of_life_utils import QOL


class ActiveAuctions:
    class Functions:

        @staticmethod
        def get_names_of_items_to_bid(connection):
            read_query = "SELECT item_name FROM median_values;"
            names = MySQL.Functions.read_query(connection, read_query)
            return names

        @staticmethod
        def get_item_median_price(connection, item_name):
            read_query = f"SELECT median FROM median_values WHERE item_name='{item_name}'"
            median_value = MySQL.Functions.read_query(connection, read_query)
            return median_value[0][0]

        @staticmethod
        def change_active_auction_dict_to_class(auction):
            return MySQL.Objects.ActiveAuctionItem(
                auction_id=auction["uuid"],
                item_name=AuctionHouse.add_suffix_to_name_based_on_item_bytes(auction["item_name"].replace("'", "`"),
                                                                              auction["item_bytes"]),
                price=auction["starting_bid"],
                start_date=QOL.epoch_to_datetime_from_miliseconds(auction["start"]),
                end_date=QOL.epoch_to_datetime_from_miliseconds(auction["end"]),
                extra_info=AuctionHouse.get_extra_info_from_item_bytes(auction["item_bytes"]),
                amount=AuctionHouse.get_item_count_from_item_bytes(auction["item_bytes"]),
                BIN=auction["bin"])

        @classmethod
        def reset_all_active_auctions(cls, connection):
            saved_active_auctions = MySQL.Functions.get_active_auctions_table(connection)
            saved_auctions_ids = []
            for row in saved_active_auctions:
                saved_auctions_ids.append(row.auction_id)

            total_pages: int = cls.get_new_auctions(page=0)["totalPages"]
            for i in range(total_pages):
                print("page", i)
                current_page = cls.get_new_auctions(page=i)
                if current_page["success"]:
                    for active_auction in current_page["auctions"]:
                        active_auction = cls.change_active_auction_dict_to_class(active_auction)
                        if active_auction.auction_id not in saved_auctions_ids:
                            cls.insert_item_into_sql_if_it_is_interesting(connection, active_auction)
                            saved_auctions_ids.append(active_auction.auction_id)
                time.sleep(1)

        @classmethod
        def get_all_active_auctions(cls):
            total_pages: int = cls.get_new_auctions(page=0)["totalPages"]

            all_auctions = []
            used_auction_ids = []
            for i in range(total_pages):
                print("page", i)
                auction_page = cls.get_new_auctions(page=i)
                if auction_page["success"]:
                    for auction in auction_page["auctions"]:
                        auction = cls.change_active_auction_dict_to_class(auction)
                        if auction.auction_id not in used_auction_ids:
                            all_auctions.append(auction)
                            used_auction_ids.append(auction.auction_id)
            print(len(all_auctions))
            return all_auctions

        @classmethod
        def get_new_auctions(cls, page: int):
            try:
                return requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()
            except:
                time.sleep(120)
                cls.get_new_auctions(page)

        @classmethod
        def insert_item_into_sql_if_it_is_interesting(cls, connection, auction: MySQL.Objects.ActiveAuctionItem) -> bool:
            if cls.is_item_interesting(auction):
                # print(auction["item_name"], "coins:", auction["starting_bid"])
                MySQL.Functions.insert_active_auction_item_data(
                    connection,
                    auction_id=auction.auction_id,
                    item_name=auction.item_name,
                    price=auction.price,
                    start_time=auction.start_date,
                    end_time=auction.end_date,
                    extra_info=auction.extra_info,
                    amount=auction.amount)
                return True
            return False

        @classmethod
        def touple_list_to_string_list(cls, touple_list):
            def xxx(name: tuple):
                return name[0]

            string_list = list(map(xxx, touple_list))
            return string_list

        @classmethod
        def get_page_amount(cls):
            return cls.get_new_auctions(page=0)["totalPages"]

        @staticmethod
        def is_auction_new(last_checked_auction: datetime, new_auction: datetime):
            return new_auction > last_checked_auction

        @staticmethod
        def is_item_interesting(auction: MySQL.Objects.ActiveAuctionItem):
            return auction.BIN is True and auction.price >= 100000
