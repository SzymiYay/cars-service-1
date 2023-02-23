from decimal import Decimal

from cars_app.car.model import Car, Color
from cars_app.data_loader.cars_loader import get_cars

import pytest
import unittest


class TestCarsLoader(unittest.TestCase):

    def setUp(self) -> None:
        self.cars = [
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

    def test_get_cars(self):
        expected_result = [Car('BMW', Decimal('120'), 1500, Color.BLACK, ['ABS', 'ALLOY WHEELS']),
                           Car('MAZDA', Decimal('160'), 2500, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH'])]
        result = get_cars(self.cars)

        self.assertListEqual(result, expected_result)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].model, 'BMW')
        self.assertEqual(result[0].price, Decimal('120'))
        self.assertEqual(result[0].mileage, 1500)
        self.assertEqual(result[0].color, Color.BLACK)
        self.assertListEqual(result[0].components, ['ABS', 'ALLOY WHEELS'])
        self.assertEqual(result[1].model, 'MAZDA')
        self.assertEqual(result[1].price, Decimal('160'))
        self.assertEqual(result[1].mileage, 2500)
        self.assertEqual(result[1].color, Color.WHITE)
        self.assertListEqual(result[1].components, ['AIR CONDITIONING', 'BLUETOOTH'])


if __name__ == '__main__':
    unittest.main()
