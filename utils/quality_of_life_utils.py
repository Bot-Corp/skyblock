import datetime


class QOL:

    @staticmethod
    def epoch_to_datetime_from_miliseconds(epoch: int):
        return datetime.datetime.fromtimestamp(epoch/1000)