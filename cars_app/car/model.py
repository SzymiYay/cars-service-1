from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, IntEnum
from typing import Any


class Color(IntEnum):
    BLACK = 1
    SILVER = 2
    WHITE = 3


@dataclass
class Car:
    model: str
    price: Decimal
    mileage: int
    color: Color
    components: list[str]

    def has_mileage_greater_than(self, value: int) -> bool:
        return self.mileage > value

    def has_price_between(self, price_from: Decimal, price_to: Decimal) -> bool:
        return price_from <= self.price <= price_to

    def __str__(self):
        return f"""
            MODEL: {self.model}
            PRICE: {self.price}
            MILEAGE: {self.mileage}
            COLOR: {self.color.name}
            COMPONENTS: {", ".join(self.components)}
        """

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        car = Car(**data)
        car.price = Decimal(data['price'])
        car.color = Color[data['color']]
        return car