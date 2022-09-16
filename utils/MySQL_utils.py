import datetime

import mysql.connector
from mysql.connector import Error


class MySQL:
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


        @staticmethod
        def execute_query(connection, query):
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                connection.commit()
                print("Query successful")
            except Error as err:
                print(f"Error: '{err}'")


        @classmethod
        def insert_active_auction_item_data(cls, connection, auction_id: str, item_name: str, price: int, start_time: datetime, end_time: datetime):
            insert_query = f"INSERT INTO active_auctions VALUES('{auction_id}', '{item_name}', {price}, '{start_time}', '{end_time}');"
            cls.execute_query(connection, insert_query)


        @classmethod
        def delete_all_active_auctions_records(cls, connection):
            delete_query = "DELETE FROM active_auctions"
            cls.execute_query(connection, delete_query)