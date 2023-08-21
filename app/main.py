import flats
import geo


if __name__ == '__main__':
    print('Flat app is starting!')
    flats_data = flats.load_flats_data()
    flats_details = flats.get_flats_location_details(flats_data)
    info = geo.get_properties_geo_info(flats_details)



