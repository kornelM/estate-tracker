# import transformer
import requests
import urllib.parse
from requests.structures import CaseInsensitiveDict

from app.geo.popo.GeoInfo import GeoInfo
from app.transformer import JsonField

API_KEY = "4d1b51472655403baf0e82d963a905f9"
GEOAPI_URL_ADDRESS = "https://api.geoapify.com/v1/geocode/search?"


def get_geo_information(location_name):
    url = build_url(location_name)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/transformer"
    headers["User-Agent"] = "application/transformer"

    resp = requests.get(url, headers=headers)

    return resp.text


def build_url(location_name):
    query_params = {
        'text': location_name,
        'format': 'transformer',
        'apiKey': API_KEY
    }

    return GEOAPI_URL_ADDRESS + urllib.parse.urlencode(query_params)


def convert_to_object(given_json):
    geo_results = []
    results = given_json[JsonField.RESULTS.value]
    for result in results:
        geo_result = GeoInfo(
            result[JsonField.NAME.value],
            result[JsonField.STREET.value],
            result[JsonField.LONGITUDE.value],
            result[JsonField.LATITUDE.value],
            result[JsonField.COUNTRY.value],
            result[JsonField.STATE.value],
            result[JsonField.DISTRICT.value],
            result[JsonField.POSTCODE.value]
        )
        geo_results.append(geo_result)

    return geo_results


# if __name__ == '__main__':
#     # get_geo_information("fieldorfa-nila, kraków")
#     information = get_geo_information("sołtyka, kraków")
#     json_load = transformer.loads(information)
#     geo_objects = convert_to_object(json_load)
#     print(geo_objects)
