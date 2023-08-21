import json


class SafeObject:

    def __init__(self, given_value):
        self.__value = given_value
        super().__init__()

    @staticmethod
    def of_nullable(given_object):
        if given_object is None:
            return SafeObject(None)
        else:
            return SafeObject(given_object)

    def map_by(self, func):
        if self.get_value() is None:
            return self
        else:
            return SafeObject(func(self.get_value()))

    def get_value(self):
        return self.__value
