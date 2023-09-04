import csv

import flats
import geo
from app.common.file.FileService import write_offers_into, read_flat_geo_from_file
from app.map.MapService import plot_map_2

should_read_from_file = True

if __name__ == '__main__':
    print('Flat app is starting!')
    flats_info = flats.load_flats_data()
    flats_details_dict = {}

    if should_read_from_file:
        flats_details_dict = read_flat_geo_from_file()
    else:
        flats_details_dict = geo.get_properties_geo_info(flats_info)
        write_offers_into(flats_details_dict)

    plot_map_2(flats_details_dict)
