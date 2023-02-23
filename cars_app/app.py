from .car.service import CarsService
from .data_loader.json_loader import get_cars_data
from .data_loader.cars_loader import get_cars
from.logger.model import CustomFormatter, MyLogger
from .car.types import SortCriteria

from typing import Final

import logging

def main() -> None:
    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')
    FILENAME: Final[str] = 'cars_app/data/cars.json'

    cars_data = get_cars_data(FILENAME)
    logger.info('Successfully loaded cars data from file')
    print(cars_data)

    cars = get_cars(cars_data)

    cars_service = CarsService(cars)
    logger.info('Successfully created CarsService')

    logger.debug('String representation of cars')
    print(cars_service)


