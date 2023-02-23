from cars_app.data_loader.json_loader import get_cars_data


import unittest
import json


class TestJSONLoader(unittest.TestCase):

    def test_get_cars_data(self):
        expected_result = [
            {
                'model': 'BMW',
                'price': 120,
                'color': 'BLACK',
                'mileage': 1500,
                'components': ['ABS', 'ALLOY WHEELS']
            },
            {
                'model': 'MAZDA',
                'price': 160,
                'color': 'WHITE',
                'mileage': 2500,
                'components': ['AIR CONDITIONING', 'BLUETOOTH']
            }
        ]
        result = get_cars_data('cars_app/data/cars.json')

        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
