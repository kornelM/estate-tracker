import csv

filename = './data/flats.csv'


def write_flats_into(flats):
    header_line = flats_csv_header_line()
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file, quotechar='"')
            writer.writerow(header_line)
            for flat in flats:
                writer.writerow(
                    [
                        flat.id,
                        flat.title,
                        flat.transaction_type,
                        flat.total_price,
                        flat.rooms_number,
                        flat.city,
                        flat.currency,
                        flat.street,
                        flat.estate_type,
                        flat.location_label,
                        flat.is_private_owner,
                        flat.agency,
                        flat.is_exclusive_offer,
                        flat.is_promoted,
                        flat.area_in_square_meters,
                        flat.rent_price,
                        flat.terrain_area_in_square_meters,
                        flat.price_per_square_meter,
                        flat.date_created_first,
                    ]
                )
    except BaseException as e:
        print('BaseException: ' + filename + ', exception message: ' + str(e))
    else:
        print('Flats data has been written down to file successfully. Flats in file: ' + str(len(flats)))


def flats_csv_header_line():
    return [
        'id',
        'title',
        'transaction_type',
        'total_price',
        'rooms_number',
        'city',
        'currency',
        'street',
        'estate_type',
        'location_label',
        'is_private_owner',
        'agency',
        'is_exclusive_offer',
        'is_promoted',
        'area_in_square_meters',
        'rent_price',
        'terrain_area_in_square_meters',
        'price_per_square_meter',
        'date_created_first'
    ]
