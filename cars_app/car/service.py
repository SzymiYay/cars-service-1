from .model import Car, Color

from dataclasses import dataclass


@dataclass
class CarsService:
    cars: list[Car]
