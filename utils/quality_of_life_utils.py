import datetime
import re


class QOL:

    @staticmethod
    def epoch_to_datetime_from_miliseconds(epoch: int):
        return datetime.datetime.fromtimestamp(epoch/1000)

    @staticmethod
    def take_out_int_from_str(string: str):  # returns first int in string
        return int(re.search(r'\d+', string).group())