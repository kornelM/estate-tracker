class FlatDetails:

    def __init__(self,
                 id,
                 latitude,
                 longitude
                 ):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        super().__init__()

    # def __eq__(self, other):
    #     return isinstance(other, self.__class__) \
    #         and self.id == other.id \
    #         and self.street == other.street \
    #         and self.city == other.city

    # def __hash__(self) -> int:
    #     return hash((self.id, self.street, self.city))
