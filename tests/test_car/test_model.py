import cars_app.car.model as c

from decimal import Decimal
import pytest
import unittest


class TestCar(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.car = c.Car('BMW', Decimal('150000'), 160_000, c.Color.WHITE, ['cos'])

    def test_mileage_greater_than_value(self):
        result = self.car.has_mileage_greater_than(150_000)
        self.assertTrue(result)

    def test_mileage_less_than_value(self):
        result = self.car.has_mileage_greater_than(180_000)
        self.assertFalse(result)

    def test_price_in_range(self):
        result = self.car.has_price_between(Decimal('130_000'), Decimal('190_000'))
        self.assertTrue(result)

    def test_price_not_in_range(self):
        result = self.car.has_price_between(Decimal('200_000'), Decimal('250_000'))
        self.assertFalse(result)

    def test_from_dict(self):
        data = {
            "model": "BMW",
            "price": 120,
            "color": "BLACK",
            "mileage": 1500,
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ]
        }
        expected_result = c.Car('BMW', Decimal('120'), 1500, c.Color.BLACK, ["ABS", "ALLOY WHEELS"])
        result = c.Car.from_dict(data)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
