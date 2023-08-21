from app.flats.popo.FlatInfo import FlatInfo
from app.transformer import JsonField
from app.common import SafeObject


def convert_to_list(given_json):
    flats = []
    offers = given_json[JsonField.OFFERS.value]
    for offer in offers:
        items = offer[JsonField.VALUE.value][JsonField.PAGE_PROPS.value][JsonField.DATA.value][
            JsonField.SEARCH_ADS.value][JsonField.ITEMS.value]
        for item in items:
            flat_info = FlatInfo(
                item[JsonField.ID.value],
                item[JsonField.TITLE.value],
                item[JsonField.TRANSACTION.value],
                item[JsonField.ESTATE.value],
                SafeObject.of_nullable(item[JsonField.LOCATION.value]).map_by(lambda item_inside: item_inside[JsonField.ADDRESS.value]).map_by(
                    lambda item_inside: item_inside[JsonField.CITY.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                SafeObject.of_nullable(item[JsonField.LOCATION.value]).map_by(lambda item_inside: item_inside[JsonField.ADDRESS.value]).map_by(
                    lambda item_inside: item_inside[JsonField.STREET.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                SafeObject.of_nullable(item[JsonField.LOCATION_LABEL.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                item[JsonField.IS_PRIVATE_OWNER.value],
                SafeObject.of_nullable(item[JsonField.AGENCY.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                item[JsonField.IS_EXCLUSIVE_OFFER.value],
                item[JsonField.IS_PROMOTED.value],
                SafeObject.of_nullable(item[JsonField.TOTAL_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                SafeObject.of_nullable(item[JsonField.TOTAL_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.CURRENCY.value]).get_value(),
                item[JsonField.ROOMS_NUMBER.value],
                item[JsonField.AREA_IN_SQUARE_METERS.value],
                SafeObject.of_nullable(item[JsonField.RENT_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                item[JsonField.TERRAIN_AREA_IN_SQUARE_METERS.value],
                SafeObject.of_nullable(item[JsonField.PRICE_PER_SQUARE_METER.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                item[JsonField.DATE_CREATED_FIRST.value]
            )
            flats.append(flat_info)
    return flats
