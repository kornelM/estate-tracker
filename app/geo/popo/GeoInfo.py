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
