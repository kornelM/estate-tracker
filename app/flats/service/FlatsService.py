import app.common as common
import app.transformer as my_json
from app.flats.file.FlatsFileWriter import write_flats_into
from app.flats.json.FlatsJsonService import convert_to_list
from app.flats.service.StreetNameService import prepare_street_name

FILEPATH_FLATS_JSON_RAW_DATA = '/home/kornel/PycharmProjects/EstateTracker/data/output.txt'


def load_flats_data():
    flats_json = get_flats_json()
    flats = convert_to_list(flats_json)
    write_flats_into(flats)
    return flats


# def get_flats_location_details():
#     flat_details = []
#
#     for flat in flats:
#         flat_details.append(
#             FlatLocationDetails(
#                 flat.id,
#                 get_street_name(flat),
#                 flat.city
#             )
#         )
#     return flat_details


def get_street_name(flat):
    return prepare_street_name(flat)


def get_flats_json():
    json_file = common.read_file(FILEPATH_FLATS_JSON_RAW_DATA)
    return my_json.JsonService.read_file_as_json(json_file)
