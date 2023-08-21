import unittest
from unittest import TestCase

from parameterized import parameterized

from app.flats.popo.FlatInfo import FlatInfo
from app.flats.service.StreetNameService import prepare_street_name


class Test(TestCase):

    def test_should_return_street_name_from_street_field(self):
        # given
        expected = 'street name'
        flat_info = FlatInfo.__new__(FlatInfo)
        flat_info.street = expected

        # when
        returned = prepare_street_name(flat_info)

        # then

        self.assertEqual(expected, returned)

    def test_should_return_street_name_from_location_label_field_when_contains_ul(self):
        # given
        expected = 'Sołtyka'
        flat_info = FlatInfo.__new__(FlatInfo)
        flat_info.street = None
        flat_info.location_label = 'Krakow, ul. Sołtyka'

        # when
        returned = prepare_street_name(flat_info)

        # then
        self.assertEqual(expected, returned)

    @parameterized.expand(
        [
            ('Should return street when given street', 'Street', None, None, 'Street'),
            ('Should return street when given street', 'ul.Street', None, None, 'Street'),
            ('Should return street when given street', 'ul. Street', None, None, 'Street'),
            ('Should return city', None, None, 'Cracow', 'Cracow'),
            ('Should return l-l when given l-l', None, 'Location Label', None, 'Location Label'),
            ('Should return l-l when given l-l', None, 'ul.Location Label', None, 'Location Label'),
            ('Should return l-l when given l-l', None, 'ul. Location Label', None, 'Location Label'),
            ('Should return l-l when given l-l and city', None, 'Cracow, ul.Location Label', None, 'Location Label'),
            ('Should return l-l when given l-l and city', None, 'Cracow, ul. Location Label', None, 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul.Location Label',
             None, 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul. Location Label',
             None, 'Location Label'),
            ('Should return l-l when given l-l, district and city', None, 'Cracow, District Name, ul. Location Label',
             None, 'Location Label'),
            ('Should return district when given district and city', None, 'Cracow, DistrictName', None, 'DistrictName'),
            (
                    'Should return district when given district and city', None, 'Cracow, District Name', None,
                    'District Name')
        ]
    )
    def test_get_street_name_parameterized(self,
                                           name,
                                           given_street,
                                           given_location_label,
                                           city,
                                           expected):
        # given
        flat_info = FlatInfo.__new__(FlatInfo)
        flat_info.id = 1
        flat_info.street = given_street
        flat_info.location_label = given_location_label
        flat_info.city = city

        # when
        returned = prepare_street_name(flat_info)

        # then
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()
