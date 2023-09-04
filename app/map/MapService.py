import pandas as pd
import plotly.express as px

from app.flats.popo.FlatAddress import FlatAddress
from app.flats.popo.FlatInfo import FlatInfo


def plot_map_2(flats_details_dict):
    flats = []
    keys = flats_details_dict.keys()
    for key in keys:
        flat_list = flats_details_dict[key]
        for flat_info in flat_list:
            flats.append(flat_info)

    df = pd.DataFrame.from_records([c.to_dict() for c in flats])
    df.info()
    print(df[['total_price', 'latitude', 'longitude', 'district']])

    color_scale = [(0, 'orange'), (1, 'red')]

    df.dropna(
        axis=0,
        how='any',
        subset=None,
        inplace=True
    )

    fig = px.scatter_mapbox(df,
                            lat="latitude",
                            lon="longitude",
                            hover_name="title",
                            hover_data=[
                                'id',
                                'title',
                                'transaction_type',
                                'estate_type',
                                'is_private_owner',
                                # 'agency',
                                # 'is_exclusive_offer',
                                # 'is_promoted',
                                'total_price',
                                'currency',
                                'rooms_number',
                                'area_in_square_meters',
                                'rent_price',
                                'terrain_area_in_square_meters',
                                'price_per_square_meter',
                                'date_created_first',
                                'street',
                                'district',
                                # 'city',
                                # 'location_label',
                                'longitude',
                                'state',
                                'postcode',
                                'latitude'
                            ],
                            color="price_per_square_meter",
                            color_continuous_scale=color_scale,
                            size="area_in_square_meters",
                            zoom=10,
                            height=900,
                            width=1500)

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


# fig = px.scatter_geo(df, lat='latitude', lon='longitude', hover_name="name")
# fig.update_layout(title='World map', title_x=0.5)
# fig.show()

# plt.scatter(x=df['longitude'], y=df['latitude'])
# plt.show()
# BBox = (('19.8015', '20.1383', '49.9753', '50.1267'))
# BBox = ((df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max()))
# implot = plt.imshow(image)

# put a blue dot at (10, 20)
# plt.xlim(BBox[0], BBox[1])
# plt.ylim(BBox[2], BBox[3])
# plt.scatter([10], [20])

# put a red dot, size 40, at 2 locations:
# plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)

# plt.show()
# fig, ax = plt.subplots(figsize=(7, 7))
# ax.scatter(df.latitude, df.longitude, zorder=1, alpha=0.9, c='red', s=10)
# ax.set_title('Plotting Spatial Data on Riyadh Map')
# ax.set_xlim(BBox[0], BBox[1])
# ax.set_ylim(BBox[2], BBox[3])
# plt.imshow(ruh_m, zorder=0, extent=BBox, aspect='equal')
# plt.show()


if __name__ == '__main__':
    geos = {}
    geos[("street", "city")] = [
        FlatInfo(
            id='id1',
            title="title1",
            transaction_type="transaction_type1",
            estate_type="estate_type1",
            is_private_owner="is_private_owner1",
            agency="agency1",
            is_exclusive_offer="is_exclusive_offer1",
            is_promoted="is_promoted1",
            total_price="100000",
            currency="currency1",
            rooms_number="rooms_number1",
            area_in_square_meters="area_in_square_meters1",
            rent_price="rent_price1",
            terrain_area_in_square_meters="terrain_area_in_square_meters1",
            price_per_square_meter="price_per_square_meter1",
            date_created_first="date_created_first1",
            address_details=FlatAddress(street="Sołtyka", longitude=19.948464, latitude=50.0598332, city="Kraków")
        ),
        FlatInfo(
            id='id2',
            title="title2",
            transaction_type="transaction_type2",
            estate_type="estate_type2",
            is_private_owner="is_private_owner2",
            agency="agency2",
            is_exclusive_offer="is_exclusive_offer2",
            is_promoted="is_promoted2",
            total_price="150000",
            currency="currency2",
            rooms_number="rooms_number2",
            area_in_square_meters="area_in_square_meters2",
            rent_price="rent_price2",
            terrain_area_in_square_meters="terrain_area_in_square_meters2",
            price_per_square_meter="price_per_square_meter2",
            date_created_first="date_created_first2",
            address_details=FlatAddress(street="mogilska 55", longitude=19.9649509, latitude=50.0666381, city="Kraków")
        )]
    geos[("street2", "city")] = [
        FlatInfo(
            id='id3',
            title="title3",
            transaction_type="transaction_type3",
            estate_type="estate_type3",
            is_private_owner="is_private_owner3",
            agency="agency3",
            is_exclusive_offer="is_exclusive_offer3",
            is_promoted="is_promoted3",
            total_price="200000",
            currency="currency3",
            rooms_number="rooms_number3",
            area_in_square_meters="area_in_square_meters3",
            rent_price="rent_price3",
            terrain_area_in_square_meters="terrain_area_in_square_meters3",
            price_per_square_meter="price_per_square_meter3",
            date_created_first="date_created_first3",
            address_details=FlatAddress(street="Fieldorfa Nila 9", longitude=19.935270440036113, latitude=50.08830385, city="Kraków")
        )
    ]
    geos[("street3", "city")] = [
        FlatInfo(
            id='id4',
            title="title4",
            transaction_type="transaction_type4",
            estate_type="estate_type4",
            is_private_owner="is_private_owner4",
            agency="agency4",
            is_exclusive_offer="is_exclusive_offer4",
            is_promoted="is_promoted4",
            total_price="210000",
            currency="currency4",
            rooms_number="rooms_number4",
            area_in_square_meters="area_in_square_meters4",
            rent_price="rent_price4",
            terrain_area_in_square_meters="terrain_area_in_square_meters4",
            price_per_square_meter="price_per_square_meter4",
            date_created_first="date_created_first4",
            address_details=FlatAddress(street="Topolowa 48", latitude=50.0664222, longitude=19.9563881, city="Kraków")
        )
    ]
    plot_map_2(geos)
    print("END")
