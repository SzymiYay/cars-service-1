from dataclasses import dataclass


@dataclass
class Car:
    id: int | None = None
    model: str | None = None
    price: int | None = 0
    color: str | None = None
    mileage: int | None = None
