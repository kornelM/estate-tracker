class GeoInfo:

    def __init__(self,
                 name,
                 street,
                 longitude,
                 latitude,
                 country,
                 state,
                 district,
                 postcode):
        self.name = name
        self.street = street
        self.longitude = longitude
        self.latitude = latitude
        self.country = country
        self.state = state
        self.district = district
        self.postcode = postcode
        super().__init__()

    def to_dict(self):
        return {
            'name': self.name,
            'street': self.street,
            'longitude': float(self.longitude),
            'latitude': float(self.latitude),
            'price': float(self.latitude) + 50.0
        }
