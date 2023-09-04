class FlatAddress:

    def __init__(self,
                 street=None,
                 district=None,
                 city=None,
                 location_label=None,
                 longitude=None,
                 state=None,
                 postcode=None,
                 latitude=None):
        self.id = id
        self.street = street
        self.district = district
        self.location_label = location_label
        self.city = city
        self.postcode = postcode
        self.longitude = longitude
        self.state = state
        self.latitude = latitude
        super().__init__()

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.id == other.id \
            and self.street == other.street \
            and self.city == other.city

    def __hash__(self) -> int:
        return hash((self.id, self.street, self.city))
