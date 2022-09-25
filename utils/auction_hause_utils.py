import base64
import io
from typing import List

import nbt as nbt

from utils.MySQL_utils import MySQL
from utils.quality_of_life_utils import QOL


class AuctionHouse:
    @staticmethod
    def decode_item_bytes_data(raw_data) -> str:
        data = nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw_data)))
        return data.pretty_tree()

    @classmethod
    def get_item_count_from_item_bytes(cls, raw_data) -> int:
        data = cls.decode_item_bytes_data(raw_data)
        count_key_string = data.split("Count")[1]
        item_count = QOL.take_out_int_from_str(count_key_string)

        return item_count

    @classmethod
    def get_extra_info_from_item_bytes(cls, item_bytes) -> str:
        if cls.Enchants.check_if_item_has_enchantments(item_bytes):
            return cls.Enchants.get_item_enchantments_from_item_bytes(item_bytes)

        if cls.Pets.check_if_item_is_a_pet_from_item_bytes(item_bytes):
            if cls.Pets.check_if_pet_has_a_held_item_from_item_bytes(item_bytes):
                return cls.Pets.get_pet_held_item_from_item_bytes(item_bytes)

        return ""

    class Enchants:
        @classmethod
        def check_if_item_has_enchantments(cls, item_bytes) -> bool:
            data = AuctionHouse.decode_item_bytes_data(item_bytes)
            if "TAG_Compound('enchantments'): {0 Entries}" in data:
                return False

            return "TAG_Compound('enchantments')" in data

        @classmethod
        def get_item_enchantments_from_item_bytes(cls, raw_data) -> str:
            data = AuctionHouse.decode_item_bytes_data(raw_data)
            enchantments_string = data.split("TAG_Compound('enchantments')")[1]
            enchantments_list = cls.__get_enchantment_string_after_splits(enchantments_string)
            enchants = cls.__fuse_enchantment_tiers_and_names_together(enchantments_list)
            enchants = ", ".join(enchants)

            return enchants

        @staticmethod
        def __get_enchantment_string_after_splits(enchantment_string) -> str:
            ench_entries = enchantment_string.split("Entries}")[1]
            ench_list = ench_entries.split("}")[0]
            ench_list = ench_list.replace("{", "")
            ench_list = ench_list.replace("TAG_Int('", "")
            ench_list = ench_list.replace("'):", "")
            ench_list = ench_list.split()

            return ench_list

        @staticmethod
        def __fuse_enchantment_tiers_and_names_together(enchantment_list) -> List[str]:
            complete_enchants = []
            provisional_string = ""
            if len(enchantment_list) % 2 == 0:
                for element in enchantment_list:
                    if provisional_string == "":
                        provisional_string += element
                    else:
                        provisional_string += " " + element
                        complete_enchants.append(provisional_string.capitalize())
                        provisional_string = ""
            else:
                print(enchantment_list)
                raise Exception("niepoprawne enchanty!")

            return complete_enchants

    class Pets:
        @classmethod
        def add_pet_rarity_to_name_if_item_is_a_pet(cls, name: str, item_bytes: str) -> str:
            if cls.check_if_item_is_a_pet_from_item_bytes(item_bytes):
                return name + " " + cls.get_pet_rarity_from_item_bytes(item_bytes)

            return name

        @classmethod
        def check_if_item_is_a_pet_from_item_bytes(cls, item_bytes):
            data = AuctionHouse.decode_item_bytes_data(item_bytes)
            return "petInfo'):" in data

        @classmethod
        def check_if_pet_has_a_held_item_from_item_bytes(cls, item_bytes: str) -> bool:
            data = AuctionHouse.decode_item_bytes_data(item_bytes)
            pet_info = cls.__get_pet_info_dict_from_decoded_string(data)

            return "heldItem" in pet_info

        @classmethod
        def get_pet_rarity_from_item_bytes(cls, item_bytes: str) -> str:
            decoded_string = AuctionHouse.decode_item_bytes_data(item_bytes)
            pet_info = cls.__get_pet_info_dict_from_decoded_string(decoded_string)

            return pet_info["tier"].capitalize()

        @classmethod
        def get_pet_held_item_from_item_bytes(cls, item_bytes: str) -> str:
            decoded_string = AuctionHouse.decode_item_bytes_data(item_bytes)
            pet_info = cls.__get_pet_info_dict_from_decoded_string(decoded_string)

            return pet_info["heldItem"]

        @staticmethod
        def __get_pet_info_dict_from_decoded_string(decoded_data) -> dict:
            xxx = decoded_data.split("petInfo'): ")
            pet_info_str = xxx[1].split("}")[0] + "}"
            pet_info_str = pet_info_str.replace("false", "False")
            pet_info_str = pet_info_str.replace("true", "True")
            try:
                pet_info_dict = eval(pet_info_str)
                return pet_info_dict
            except:
                try:
                    pet_info_dict = eval(pet_info_str + "}")
                    return pet_info_dict
                except Exception as e:
                    print("ERROR:", e)
                    print(pet_info_str)

        @staticmethod
        def get_all_pets_queries(connection) -> List[MySQL.Objects.FinishedAuctionItem]:
            all_pets_query = "SELECT * from finished_auctions WHERE item_name LIKE '[Lvl%';"
            all_pets = MySQL.Functions.read_query(connection, all_pets_query)

            list_of_items = []
            for item in all_pets:
                list_of_items.append(MySQL.Objects.FinishedAuctionItem(
                    auction_id=item[0],
                    item_name=item[1],
                    price=item[2],
                    start_date=item[3],
                    end_date=item[4],
                    buyer=item[5],
                    seller=item[6],
                    item_bytes=item[7],
                ))

            return list_of_items
