import random
import string

from app.flats.popo.FlatAddress import FlatAddress


class FlatInfo:

    def __init__(self,
                 id,
                 title,
                 transaction_type,
                 estate_type,
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
                 date_created_first,
                 address_details: [FlatAddress] = None
                 ):
        self.id = id
        self.title = title
        self.transaction_type = transaction_type
        self.estate_type = estate_type
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
        self.address_details: [FlatAddress] = address_details
        super().__init__()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'transaction_type': self.transaction_type,
            'estate_type': self.estate_type,
            'is_private_owner': self.is_private_owner,
            # 'agency': self.agency,
            # 'is_exclusive_offer': self.is_exclusive_offer,
            # 'is_promoted': self.is_promoted,
            'total_price': self._get_or_default_float(self.total_price),
            'currency': self.currency,
            'rooms_number': self.rooms_number,
            'area_in_square_meters': self._get_or_default_float(self.area_in_square_meters),
            'rent_price': self._get_or_default_float(self.rent_price),
            'terrain_area_in_square_meters': self._get_or_default_float(self.terrain_area_in_square_meters),
            'price_per_square_meter': self._get_or_default_float(self.price_per_square_meter),
            'date_created_first': self.date_created_first,
            'street': self._get_or_default_string(self.address_details.street),
            'district': self._get_or_default_string(self.address_details.district),
            'city': self._get_or_default_string(self.address_details.city),
            # 'location_label': self.address_details.location_label,
            'longitude': self._get_or_default_float(self.address_details.longitude),
            'state': self._get_or_default_string(self.address_details.state),
            'postcode': self._get_or_default_string(self.address_details.postcode),
            'latitude': self._get_or_default_float(self.address_details.latitude)
        }

    @staticmethod
    def _get_or_default_string(value):
        if value is None:
            return 'no data'
        return value

    @staticmethod
    def _get_or_default_float(value):
        if value is None or value is '':
            return float(0.0)
        return float(value)



if __name__ == '__main__':
    print('Flat app is starting!')
    for r in str('a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a').split(','):
        print(random.uniform(0.005, 0.01))
