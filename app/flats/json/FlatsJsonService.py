from app.flats.popo.FlatAddress import FlatAddress
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
                id=item[JsonField.ID.value],
                title=item[JsonField.TITLE.value],
                transaction_type=item[JsonField.TRANSACTION.value],
                estate_type=item[JsonField.ESTATE.value],
                is_private_owner=item[JsonField.IS_PRIVATE_OWNER.value],
                agency=SafeObject.of_nullable(item[JsonField.AGENCY.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                is_exclusive_offer=item[JsonField.IS_EXCLUSIVE_OFFER.value],
                is_promoted=item[JsonField.IS_PROMOTED.value],
                total_price=SafeObject.of_nullable(item[JsonField.TOTAL_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                currency=SafeObject.of_nullable(item[JsonField.TOTAL_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.CURRENCY.value]).get_value(),
                rooms_number=item[JsonField.ROOMS_NUMBER.value],
                area_in_square_meters=item[JsonField.AREA_IN_SQUARE_METERS.value],
                rent_price=SafeObject.of_nullable(item[JsonField.RENT_PRICE.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                terrain_area_in_square_meters=item[JsonField.TERRAIN_AREA_IN_SQUARE_METERS.value],
                price_per_square_meter=SafeObject.of_nullable(item[JsonField.PRICE_PER_SQUARE_METER.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value(),
                date_created_first=item[JsonField.DATE_CREATED_FIRST.value],
                address_details=FlatAddress(
                    street=SafeObject.of_nullable(item[JsonField.LOCATION.value]).map_by(lambda item_inside: item_inside[JsonField.ADDRESS.value]).map_by(
                        lambda item_inside: item_inside[JsonField.STREET.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                    city=SafeObject.of_nullable(item[JsonField.LOCATION.value]).map_by(lambda item_inside: item_inside[JsonField.ADDRESS.value]).map_by(
                        lambda item_inside: item_inside[JsonField.CITY.value]).map_by(lambda item_inside: item_inside[JsonField.NAME.value]).get_value(),
                    location_label=SafeObject.of_nullable(item[JsonField.LOCATION_LABEL.value]).map_by(lambda item_inside: item_inside[JsonField.VALUE.value]).get_value()
                )
            )
            flats.append(flat_info)
    return flats
