from cars_app.car.service import CarsService
from cars_app.car.model import Car, Color
from cars_app.car.types import SortCriteria

from decimal import Decimal

import pytest
import unittest


class TestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cars = CarsService(
            [
                Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])
            ]
        )

    def test_sorted_by_model(self):
        expected_result = [Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH']),
                           Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                           Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO'])]
        result = self.cars.sort_by(SortCriteria.MODEL)

        self.assertListEqual(result, expected_result)

    def test_sorted_by_price(self):
        expected_result = [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                           Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.sort_by(SortCriteria.PRICE)

        self.assertListEqual(result, expected_result)

    #
    def test_sorted_by_mileage(self):
        expected_result = [Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                           Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.sort_by(SortCriteria.MILEAGE)

        self.assertListEqual(result, expected_result)

    #
    def test_sorted_by_color(self):
        expected_result = [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH']),
                           Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO'])]
        result = self.cars.sort_by(SortCriteria.COLOR)

        self.assertListEqual(result, expected_result)

    def test_no_car_with_mileage_greater_than_value(self):
        value = 50000

        expected_result = []
        result = self.cars.get_cars_with_mileage_greater_than(value)

        self.assertListEqual(result, expected_result)

    def test_cars_with_mileage_greater_than_value(self):
        value = 20000

        expected_result = [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.get_cars_with_mileage_greater_than(value)

        self.assertListEqual(result, expected_result)

    def test_get_color_and_no_of_cars(self):
        expected_result = {
            'BLACK': 1,
            'SILVER': 1,
            'WHITE': 1
        }
        result = self.cars.get_color_and_no_of_cars()

        self.assertDictEqual(result, expected_result)

    def test_get_model_and_most_expensive_car(self):
        cars = CarsService(
            [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'ALLOY WHEELS']),
             Car('BMW', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH']),
             Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        )

        expected_result = {
            'AUDI': Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH']),
            'BMW': Car('BMW', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH'])
        }
        result = cars.get_model_and_most_expensive_car()

        self.assertDictEqual(result, expected_result)

    def test_get_most_expensive_car(self):
        cars = CarsService(
            [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'ALLOY WHEELS']),
             Car('BMW', Decimal('200'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH']),
             Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        )

        expected_result = [Car('BMW', Decimal('200'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = cars.get_most_expensive_cars()

        self.assertListEqual(result, expected_result)

    def test_get_most_expensive_car2(self):
        expected_result = [Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.get_most_expensive_cars()

        self.assertListEqual(result, expected_result)

    def test_get_most_expensive_cars(self):
        cars = CarsService(
            [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'HEATING', 'ALLOY WHEELS']),
             Car('MAZDA', Decimal('200'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
             Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        )
        expected_result = [Car('MAZDA', Decimal('200'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = cars.get_most_expensive_cars()

        self.assertListEqual(result, expected_result)

    def test_get_cars_with_sorted_components(self):
        expected_result = [Car('BMW', Decimal('120'), 25000, Color.BLACK, ['ABS', 'ALLOY WHEELS', 'HEATING']),
                           Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.get_cars_with_sorted_components()

        self.assertListEqual(result, expected_result)

    def test_cars_with_price_in_range(self):
        price_from = Decimal('140')
        price_to = Decimal('220')

        expected_result = [Car('MAZDA', Decimal('160'), 15000, Color.WHITE, ['AIR CONDITIONING', 'BLUETOOTH', 'RADIO']),
                           Car('AUDI', Decimal('200'), 35000, Color.SILVER, ['BLUETOOTH'])]
        result = self.cars.get_cars_with_price_between(price_from, price_to)

        self.assertListEqual(result, expected_result)

    def test_no_cars_with_price_in_range(self):
        price_from = Decimal('80')
        price_to = Decimal('100')

        expected_result = []
        result = self.cars.get_cars_with_price_between(price_from, price_to)

        self.assertListEqual(result, expected_result)

    def test_incorrect_price_range(self):
        with self.assertRaises(ValueError) as e:
            price_from = Decimal('180')
            price_to = Decimal('100')
            self.cars.get_cars_with_price_between(price_from, price_to)

        self.assertEqual('Price range is not correct', str(e.exception))

    def test_count_cars_with_given_color(self):
        expected_result = 1
        result = self.cars._count_cars_with_given_color(Color.BLACK)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
