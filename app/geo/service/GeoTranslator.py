# import transformer
import json
import random

import requests
import urllib.parse
from requests.structures import CaseInsensitiveDict

from app.common.popo.SafeObject import SafeObject
from app.geo.popo.GeoInfo import GeoInfo
from app.transformer import JsonField

API_KEY = "4d1b51472655403baf0e82d963a905f9"
GEOAPI_URL_ADDRESS = "https://api.geoapify.com/v1/geocode/search?"


def get_geo_information(flats_details_dict):
    address_city_tuples = flats_details_dict.keys()

    addresses_to_remove = []
    for address_tuple in address_city_tuples:
        resp = perform_request(address_tuple)
        geo_info = convert_to_object(json.loads(resp.text))
        if geo_info is None:
            addresses_to_remove.append(address_tuple)
            print("passing, no info")
        else:
            if address_tuple[0] is not None and 'Turniejowa' in address_tuple[0]:
                set_missing_address_details(flats_details_dict[address_tuple], geo_info)
            set_missing_address_details(flats_details_dict[address_tuple], geo_info)
            print("set missing details for tuple: " + str(address_tuple))

    print("Dict size before removing: " + str(len(flats_details_dict)))
    print("Addresses to remove size: " + str(len(addresses_to_remove)))
    print("Dict size after removing: " + str(len(flats_details_dict)))
    for atr in addresses_to_remove:
        removed = flats_details_dict.pop(atr)
        print("passing, no info, removed: " + str(removed))
    return flats_details_dict


def perform_request(address_tuple):
    url = build_url(get_searched_text(address_tuple))
    resp = requests.get(url, headers=get_headers())
    print("REQUEST: " + url + ", RESPONSE: " + str(resp.json()))
    return resp


def set_missing_address_details(flat_info_list, geo_info):
    for flat_info in flat_info_list:
        r = random.uniform(0.0002, 0.0009)
        sign_long = random.randint(0, 2)
        sign_lat = random.randint(0, 2)

        if sign_long > 1:
            flat_info.address_details.longitude = float(geo_info.longitude) + r
        else:
            flat_info.address_details.longitude = float(geo_info.longitude) - r

        if sign_lat > 1:
            flat_info.address_details.latitude = float(geo_info.latitude) + r
        else:
            flat_info.address_details.latitude = float(geo_info.latitude) - r

        # flat_info.address_details.longitude = float(geo_info.longitude) + r / random_int
        # flat_info.address_details.latitude = float(geo_info.latitude) + r / random_int
        flat_info.address_details.district = geo_info.district
        flat_info.address_details.postcode = geo_info.postcode


def get_headers():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/transformer"
    headers["User-Agent"] = "application/transformer"
    return headers


def get_searched_text(address_city_tuple):
    street = address_city_tuple[0]
    city = address_city_tuple[1]

    to_return = ""
    if street is not None:
        if 'ul.' in street.lower():
            street = str(street).split('ul.')[1].strip()
        to_return = street
    if city is not None:
        to_return = to_return + ", " + city

    return to_return


def build_url(location_name):
    query_params = {
        'text': location_name,
        'format': 'json',
        'limit': 1,
        'apiKey': API_KEY
    }

    return GEOAPI_URL_ADDRESS + urllib.parse.urlencode(query_params)


def convert_to_object(given_json):
    # geo_results = []
    geo_result = None
    results = given_json[JsonField.RESULTS.value]
    for result in results:
        geo_result = GeoInfo(
            result.get(JsonField.NAME.value),
            result.get(JsonField.STREET.value),
            result.get(JsonField.LONGITUDE.value),
            result.get(JsonField.LATITUDE.value),
            result.get(JsonField.COUNTRY.value),
            result.get(JsonField.STATE.value),
            result.get(JsonField.DISTRICT.value),
            result.get(JsonField.POSTCODE.value)
        )
        # geo_results.append(geo_result)

    return geo_result

# if __name__ == '__main__':
#     # get_geo_information("fieldorfa-nila, kraków")
#     information = get_geo_information("sołtyka, kraków")
#     json_load = transformer.loads(information)
#     geo_objects = convert_to_object(json_load)
#     print(geo_objects)
