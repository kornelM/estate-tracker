import unittest

from parameterized.parameterized import parameterized

from app.common.popo.FlatDetails import FlatDetails
from app.flats.service.FlatsService import get_street_name, get_flats_location_details
from app.flats.popo.FlatInfo import FlatInfo


class Test(unittest.TestCase):

    @parameterized.expand(
        [
            ('Should return street when given street', 'Street', None, 'Street'),
            ('Should return street when given street', 'ul.Street', None, 'Street'),
            ('Should return street when given street', 'ul. Street', None, 'Street'),
            ('Should return l-l when given l-l', None, 'Location Label', 'Location Label'),
            ('Should return l-l when given l-l', None, 'ul.Location Label', 'Location Label'),
            ('Should return l-l when given l-l', None, 'ul. Location Label', 'Location Label'),
            ('Should return l-l when given l-l and city', None, 'Cracow, ul.Location Label', 'Location Label'),
            ('Should return l-l when given l-l and city', None, 'Cracow, ul. Location Label', 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul.Location Label', 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul. Location Label', 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul. Location Label', 'Location Label'),
            ('Should return district when given district and city', None, 'Cracow, DistrictName', 'DistrictName'),
            ('Should return district when given district and city', None, 'Cracow, District Name', 'District Name')
        ]
    )
    def test_get_street_name_parameterized(self,
                                           name,
                                           given_street,
                                           given_location_label,
                                           expected):
        # given
        flat_info = FlatInfo.__new__(FlatInfo)
        flat_info.id = 1
        flat_info.street = given_street
        flat_info.location_label = given_location_label

        # when
        returned = get_street_name(flat_info)

        # then
        self.assertEqual(expected, returned)

    def test_should_return_None_when_street_and_location_label_are_null_or_empty(self):
        # given
        expected = str(None)
        flat_info = FlatInfo.__new__(FlatInfo)
        flat_info.id = 1
        flat_info.street = None
        flat_info.location_label = None

        # when
        returned = get_street_name(flat_info)

        # then
        self.assertEqual(expected, returned)

    def test_should_return_None_when_street_and_location_label_are_null_or_empty1(self):
        # given
        flat_info_1 = FlatInfo.__new__(FlatInfo)
        flat_info_1.id = 1
        flat_info_1.street = 'ul. Street'
        flat_info_1.location_label = 'Kraków, Grzegórzki, ul. Street'
        flat_info_1.city = 'Kraków'

        flat_info_2 = FlatInfo.__new__(FlatInfo)
        flat_info_2.id = 2
        flat_info_2.street = None
        flat_info_2.location_label = 'Marianka, Grzegórzki, ul. Danielowa Street'
        flat_info_2.city = 'Marianka'

        flat_info_list = [
            flat_info_1,
            flat_info_2
        ]

        flat_details_1 = FlatDetails(1, 'Street', 'Kraków')
        flat_details_2 = FlatDetails(2, 'Danielowa Street', 'Marianka')

        expected = [
            flat_details_1,
            flat_details_2
        ]

        # when
        returned = get_flats_location_details(flat_info_list)

        # then
        self.assertListEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()
