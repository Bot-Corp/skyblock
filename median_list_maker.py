import statistics

from utils.MySQL_utils import MySQL
from utils.active_auctions_utils import ActiveAuctions


def get_good_items_list(connection):
    read_query = 'SELECT item_name FROM finished_auctions WHERE item_name NOT LIKE "%Enchanted" GROUP BY item_name HAVING COUNT(*) >= 450 ORDER BY COUNT(*) ASC;'
    names = MySQL.Functions.read_query(connection, read_query)
    names = ActiveAuctions.Functions.touple_list_to_string_list(names)
    return names


def get_sale_record_for_a_item(connection, item):
    return MySQL.Functions.read_query(connection, f"SELECT price,amount FROM finished_auctions WHERE item_name = '{item}'")

def insert_median_to_a_table(connection, name, median_value):
    MySQL.Functions.execute_query(connection, f"INSERT INTO median_values VALUES('{name}', {median_value})")

def xxx(name: tuple):
    return name[0]


connection = MySQL.Functions.connect_to_skyblock_database()

MySQL.Functions.execute_query(connection, "DELETE FROM median_values;")
names = get_good_items_list(connection)

medians_list = []
for name in names:
    median = []
    print(name)
    prices = get_sale_record_for_a_item(connection, name)
    for price in prices:
        recorded_price = price[0]
        amount = price[1]
        for i in range(amount):
            median.append(recorded_price / amount)
    median_value = statistics.median(median)
    print(median_value)
    insert_median_to_a_table(connection, name, median_value)
print(len(names))
