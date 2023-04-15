from ..car.model import Car
from ..car.validator import CarValidator
from typing import Any


def get_cars(cars_data: list[dict[str, Any]]) -> list[Car]:
    return [Car.from_dict(car_data) for car_data in cars_data if CarValidator().validate(car_data)]
