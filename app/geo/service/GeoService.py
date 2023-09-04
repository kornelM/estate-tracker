from typing import List

from app.common import FlatLocationDetails
from app.flats.popo.FlatInfo import FlatInfo
from app.geo.service import GeoTranslator
from app.map.MapService import plot_map_2


# def get_properties_geo_info(flats_details: [List[FlatLocationDetails]]):
def is_flat_info_missing_values(flat_info: [FlatInfo]):
    if flat_info.total_price is None \
            or flat_info.rooms_number is None \
            or flat_info.address_details.city is None \
            or flat_info.address_details.district is None \
            or flat_info.address_details.street is None \
            or flat_info.address_details.longitude is None \
            or flat_info.address_details.latitude is None \
            or flat_info.address_details.state is None \
            or flat_info.address_details.postcode is None \
            or flat_info.total_price is None \
            or flat_info.currency is None \
            or flat_info.is_private_owner is None \
            or flat_info.transaction_type is None:
        return True
    else:
        return False


def get_properties_geo_info(flats_info_list: List[FlatInfo]):
    flats_details_dict = {}
    counter = 0
    for flat_info in flats_info_list:
        if is_flat_info_missing_values(flat_info) is None:
            pass
            print("passing due to missing important field: " + str(flat_info.to_dict()))
            counter = counter + 1
            pass
        else:
            address_tuple_index = (flat_info.address_details.street, flat_info.address_details.city)
            if address_tuple_index in flats_details_dict.keys():
                flats_details_dict[address_tuple_index].append(flat_info)
            else:
                flats_details_dict[address_tuple_index] = [flat_info]
    print("Properties with missing fields: " + str(counter))
    return GeoTranslator.get_geo_information(flats_details_dict)


if __name__ == '__main__':
    flats_details = [
        FlatLocationDetails(1, 'Sołtyka', 'Kraków'),
        FlatLocationDetails(2, 'Fieldorfa Nila', 'Kraków'),
        FlatLocationDetails(3, 'Azory', 'Kraków'),
        FlatLocationDetails(4, 'Sołtyka', 'Kraków'),
        FlatLocationDetails(5, 'Fieldorfa Nila', 'Kraków'),
        FlatLocationDetails(6, 'Azory', 'Kraków')
    ]
    coordinates = get_properties_geo_info(flats_details)
    plot_map_2(coordinates)

    print('end')
