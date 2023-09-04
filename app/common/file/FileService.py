import csv

from app import common
import pandas as pd
from csv import DictReader

from app.flats.popo.FlatAddress import FlatAddress
from app.flats.popo.FlatInfo import FlatInfo

file_name = '/home/kornel/PycharmProjects/EstateTracker/data/flats_geo_info.csv'


def read_file(filepath):
    file = open(filepath)
    return file


def flats_geo_csv_header_line():
    return [
        'id',
        'title',
        'transaction_type',
        'estate_type',
        'is_private_owner',
        'agency',
        'is_exclusive_offer',
        'is_promoted',
        'total_price',
        'currency',
        'rooms_number',
        'area_in_square_meters',
        'rent_price',
        'terrain_area_in_square_meters',
        'price_per_square_meter',
        'date_created_first',
        'street',
        'district',
        'city',
        'longitude',
        'state',
        'postcode',
        'latitude'
    ]


def write_offers_into(flats_details_dict):
    flats = []
    keys = flats_details_dict.keys()
    for key in keys:
        flat_list = flats_details_dict[key]
        for flat_info in flat_list:
            flats.append(flat_info)

    header_line = flats_geo_csv_header_line()
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file, quotechar='"')
            writer.writerow(header_line)
            for flat in flats:
                writer.writerow(
                    [
                        flat.id,
                        flat.title,
                        flat.transaction_type,
                        flat.estate_type,
                        flat.is_private_owner,
                        flat.agency,
                        flat.is_exclusive_offer,
                        flat.is_promoted,
                        flat.total_price,
                        flat.currency,
                        flat.rooms_number,
                        flat.area_in_square_meters,
                        flat.rent_price,
                        flat.terrain_area_in_square_meters,
                        flat.price_per_square_meter,
                        flat.date_created_first,
                        flat.address_details.street,
                        flat.address_details.district,
                        flat.address_details.city,
                        flat.address_details.longitude,
                        flat.address_details.state,
                        flat.address_details.postcode,
                        flat.address_details.latitude
                    ]
                )
    except BaseException as e:
        print('BaseException: ' + file_name + ', exception message: ' + str(e))
    else:
        print('Flats data has been written down to file successfully. Flats in file: ' + str(len(flats)))


def read_flat_geo_from_file():
    flats_details_dict = {}
    flat_geo_list = _read_flat_geo_from_file()

    for flat_info in flat_geo_list:
        address_tuple_index = (flat_info.address_details.street, flat_info.address_details.city)
        if address_tuple_index in flats_details_dict.keys():
            flats_details_dict[address_tuple_index].append(flat_info)
        else:
            flats_details_dict[address_tuple_index] = [flat_info]
    return flats_details_dict


def _read_flat_geo_from_file():
    flats_geo = []
    with open(file_name, 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            flats_geo.append(
                FlatInfo(
                    id=row['id'],
                    title=row['title'],
                    transaction_type=row['transaction_type'],
                    estate_type=row['estate_type'],
                    is_private_owner=row['is_private_owner'],
                    agency=row['agency'],
                    is_exclusive_offer=row['is_exclusive_offer'],
                    is_promoted=row['is_promoted'],
                    total_price=row['total_price'],
                    currency=row['currency'],
                    rooms_number=row['rooms_number'],
                    area_in_square_meters=row['area_in_square_meters'],
                    rent_price=row['rent_price'],
                    terrain_area_in_square_meters=row['terrain_area_in_square_meters'],
                    price_per_square_meter=row['price_per_square_meter'],
                    date_created_first=row['date_created_first'],
                    address_details=FlatAddress(
                        street=row['street'],
                        district=row['district'],
                        city=row['city'],
                        longitude=row['longitude'],
                        state=row['state'],
                        postcode=row['postcode'],
                        latitude=row['latitude']
                    )
                )
            )
        return flats_geo
