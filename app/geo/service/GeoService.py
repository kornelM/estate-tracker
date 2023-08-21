from typing import List

from app.common import FlatDetails


def get_properties_geo_info(flats_details: [List[FlatDetails]]):
    flats_details_dict = {[], []}
    for flat_details in flats_details:
        if flat_details.id in flats_details_dict.keys():
            flats_details_dict.keys()
        details_id = flat_details.id
        details_street = flat_details.street
        # GeoTranslator.get_geo_information(flat_details)

    return flats_details_dict


if __name__ == '__main__':
    flats_details = [
        FlatDetails(1, 'street', 'city'),
        FlatDetails(2, 'street2', 'city2'),
        FlatDetails(3, 'street3', 'city3'),
        FlatDetails(4, 'street', 'city'),
        FlatDetails(5, 'street2', 'city2'),
        FlatDetails(6, 'street3', 'city3')
    ]
    dictionary = get_properties_geo_info(flats_details)
    print('end')
