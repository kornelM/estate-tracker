class FlatInfo:

    def __init__(self,
                 id,
                 title,
                 transaction_type,
                 estate_type,
                 city,
                 street,
                 location_label,
                 is_private_owner,
                 agency,
                 is_exclusive_offer,
                 is_promoted,
                 total_price,
                 currency,
                 rooms_number,
                 area_in_square_meters,
                 rent_price,
                 terrain_area_in_square_meters,
                 price_per_square_meter,
                 date_created_first
                 ):
        self.id = id
        self.title = title
        self.transaction_type = transaction_type
        self.estate_type = estate_type
        self.city = city
        self.street = street
        self.location_label = location_label
        self.is_private_owner = is_private_owner
        self.agency = agency
        self.is_exclusive_offer = is_exclusive_offer
        self.is_promoted = is_promoted
        self.total_price = total_price
        self.currency = currency
        self.rooms_number = rooms_number
        self.area_in_square_meters = area_in_square_meters
        self.rent_price = rent_price
        self.terrain_area_in_square_meters = terrain_area_in_square_meters
        self.price_per_square_meter = price_per_square_meter
        self.date_created_first = date_created_first
        super().__init__()
