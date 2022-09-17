import datetime
from dataclasses import dataclass
from typing import List

import mysql.connector
from mysql.connector import Error


class MySQL:
    class Objects:
        @dataclass
        class ActiveAuctionItem:
            auction_id: str
            item_name: str
            price: int
            start_date: datetime
            end_date: datetime
            item_bytes: str

    class Functions:

        @classmethod
        def connect_to_skyblock_database(cls):
            return cls.__connect_to_database("localhost", "root", "root", "skyblock")

        @staticmethod
        def __connect_to_database(host_name, user_name, user_password, database_name):
            connection = None
            try:
                connection = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    passwd=user_password,
                    database=database_name
                )
                print("MySQL Database connection successful")
            except Error as err:
                print(f"Error: '{err}'")

            return connection

        @staticmethod
        def create_database(connection, name):
            cursor = connection.cursor()
            try:
                cursor.execute(f"CREATE DATABASE {name}")
                print("Database created successfully")
            except Error as err:
                print(f"Error: '{err}'")

        @classmethod
        def insert_active_auction_item_data(cls, connection, auction_id: str, item_name: str, price: int, start_time: datetime,
                                            end_time: datetime, item_bytes: str):
            insert_query = f"INSERT INTO active_auctions VALUES('{auction_id}', '{item_name}', {price}, '{start_time}', '{end_time}', '{item_bytes}');"
            cls.execute_query(connection, insert_query)

        @classmethod
        def insert_finised_auction_item_data(cls, connection, auction_id: str, item_name: str, price: int, start_time: datetime,
                                             end_time: datetime, buyer: str, seller_profile: str, item_bytes: str):
            insert_query = f"INSERT INTO finished_auctions VALUES('{auction_id}', '{item_name}', {price}, '{start_time}', '{end_time}', '{buyer}', '{seller_profile}', '{item_bytes}');"
            cls.execute_query(connection, insert_query)

        @classmethod
        def delete_all_active_auctions_records(cls, connection):
            delete_query = "DELETE FROM active_auctions;"
            cls.execute_query(connection, delete_query)


        @classmethod
        def delete_finished_auction_from_active_auctions(cls, connection, auction_id):
            delete_query = f"DELETE FROM active_auctions WHERE auction_id='{auction_id}';"
            cls.execute_query(connection, delete_query)

        @classmethod
        def get_active_auctions_table(cls, connection):
            select_query = "SELECT * FROM active_auctions;"
            items: List[List] = cls.read_query(connection, select_query)

            list_of_items = []
            for item in items:
                list_of_items.append(MySQL.Objects.ActiveAuctionItem(
                    auction_id=item[0],
                    item_name=item[1],
                    price=item[2],
                    start_date=item[3],
                    end_date=item[4],
                    item_bytes=item[5]
                ))

            return list_of_items

        @staticmethod
        def read_query(connection, query):
            cursor = connection.cursor()
            result = None
            try:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as err:
                print(f"Error: '{err}'")

        @staticmethod
        def execute_query(connection, query):
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                connection.commit()
                print("Query successful")
            except Error as err:
                print(f"Error: '{err}'")
