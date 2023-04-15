from .model import Car, Color
from .types import SortCriteria

from dataclasses import dataclass
from decimal import Decimal
from operator import attrgetter
from collections import defaultdict
from copy import deepcopy


@dataclass
class CarsService:
    cars: list[Car]

    def sort_by(self, sort_criteria: SortCriteria, *, reverse=False) -> list[Car]:
        match sort_criteria:
            case SortCriteria.MODEL:
                return sorted(self.cars, key=lambda car: car.model, reverse=reverse)
            case SortCriteria.PRICE:
                return sorted(self.cars, key=lambda car: car.price, reverse=reverse)
            case SortCriteria.MILEAGE:
                return sorted(self.cars, key=lambda car: car.mileage, reverse=reverse)
            case SortCriteria.COLOR:
                return sorted(self.cars, key=lambda car: car.color, reverse=reverse)
            case _:
                raise ValueError('Invalid sort criteria')

    def get_cars_with_mileage_greater_than(self, value: int) -> list[Car]:
        return [car for car in self.cars if car.has_mileage_greater_than(value)]

    def get_color_and_no_of_cars(self) -> dict[Color, int]:
        return {c.name: self._count_cars_with_given_color(c) for c in Color}

    def get_model_and_most_expensive_car(self) -> dict[str, Car]:
        grouped_by_model = defaultdict(list)

        for car in self.cars:
            grouped_by_model[car.model].append(car)

        return {model: max(cars, key=lambda car: car.price) for (model, cars) in grouped_by_model.items()}

    def get_statistics(self) -> str:
        return f"""
                PRICE:
                average: {sum([car.price for car in self.cars]) / len(self.cars)}
                max: {max(self.cars, key=lambda car: car.price).price}
                min: {min(self.cars, key=lambda car: car.price).price}

                MILEAGE:
                average: {sum([car.mileage for car in self.cars]) / len(self.cars)}
                max: {max(self.cars, key=lambda car: car.mileage).mileage}
                min: {min(self.cars, key=lambda car: car.mileage).mileage}
                """

    def get_most_expensive_cars(self) -> Car | list[Car]:
        grouped_by_price = defaultdict(list)

        for car in self.cars:
            grouped_by_price[car.price].append(car)

        return max(grouped_by_price.items(), key=lambda pair: pair[0])[1]

    def get_cars_with_sorted_components(self) -> list[Car]:
        cars = deepcopy(self.cars)

        for car in cars:
            car.components.sort()

        return cars

    def get_dict_component_and_cars(self) -> dict[str, list[Car]]:
        grouped_by_component = defaultdict(list)

        for car in self.cars:
            for component in car.components:
                grouped_by_component[component].append(car)

        return dict(grouped_by_component)

    def get_cars_with_price_between(self, price_from: Decimal, price_to: Decimal) -> list[Car]:
        if price_from > price_to:
            raise ValueError('Price range is not correct')

        return [car for car in self.cars if car.has_price_between(price_from, price_to)]

    def __str__(self):
        to_string = [str(car) for car in self.cars]
        return "\n".join(to_string)

    def _count_cars_with_given_color(self, color: Color) -> int:
        return len([car for car in self.cars if car.color == color])