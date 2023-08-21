COMMA = ','
EMPTY_STRING = ''
STREET_SUFFIX = 'ul.'


def prepare_street_name(flat):
    street = flat.street
    if street is None or street == EMPTY_STRING:
        street = _prepare_street_name_from_location_label(flat)
    else:
        if STREET_SUFFIX in street:
            street_array = str(street).split(STREET_SUFFIX)
            street = street_array[1]

    return str(street).strip()


def _prepare_street_name_from_location_label(flat):
    location_label = flat.location_label
    if location_label is None or location_label == EMPTY_STRING:
        print(f"For flat id {flat.id} street not found, about to choose None type")
        street = None
    else:
        if STREET_SUFFIX in location_label:
            location_label_array = str(location_label).split(sep=STREET_SUFFIX)
            street = location_label_array[1]
        elif COMMA in location_label:
            location_label_array = str(location_label).split(sep=COMMA)
            street = location_label_array[1]
        else:
            street = location_label
    return street


