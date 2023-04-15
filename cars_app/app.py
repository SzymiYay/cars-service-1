from .car.service import CarsService
from .data_loader.json_loader import get_cars_data
from .data_loader.cars_loader import get_cars
from .logger.model import CustomFormatter, MyLogger
from .car.types import SortCriteria

from .db.model.car import Car
from .db.model.component import Component
from .db.repo.connection import MySQLConnectionPoolBuilder
from .db.repo.crud import CrudRepo
from .db.repo.car import CarRepo
from .db.repo.component import ComponentRepo

from typing import Final
from decimal import Decimal

import logging

def main() -> None:

    connection_pool = MySQLConnectionPoolBuilder().build()

    car_repo = CarRepo(connection_pool)
    component_repo = ComponentRepo(connection_pool)

    car_repo.create_table("id integer primary key auto_increment, model varchar(20) not null, price integer default 0, color varchar(50) not null, mileage integer not null")
    component_repo.create_table("id integer primary key auto_increment, name varchar(50) not null, car_id integer not null, foreign key (car_id) references cars(id) on delete cascade on update cascade")

    car_repo.insert_many()






    # """LOGGING"""
    # logger = MyLogger.get_logger()
    #
    # """APP"""
    # logger.warning('STARTING APP')
    # FILENAME: Final[str] = 'cars_app/data/cars.json'
    #
    # cars_data = get_cars_data(FILENAME)
    # logger.info('Successfully loaded cars data from file')
    # print(cars_data)
    #
    # cars = get_cars(cars_data)
    #
    # cars_service = CarsService(cars)
    # logger.info('Successfully created CarsService')
    #
    # logger.debug('String representation of cars')
    # print(cars_service)
    #
    # logger.debug('Cars sorted by specified field')
    # print(cars_service.sort_by(SortCriteria.MODEL, reverse=False))
    # print(cars_service.sort_by(SortCriteria.COLOR, reverse=True))
    # print(cars_service.sort_by(SortCriteria.PRICE, reverse=False))
    # print(cars_service.sort_by(SortCriteria.MILEAGE, reverse=False))
    #
    # logger.debug('Cars with mileage greater than 1500')
    # print(cars_service.get_cars_with_mileage_greater_than(1500))
    #
    # logger.debug('Dict with color and number of cars')
    # print(cars_service.get_color_and_no_of_cars())
    #
    # logger.debug('Dict with model and most expensive car')
    # print(cars_service.get_model_and_most_expensive_car())
    #
    # logger.debug('Statistics about cars')
    # print(cars_service.get_statistics())
    #
    # logger.debug('The most expensive cars')
    # print(cars_service.get_most_expensive_cars())
    #
    # logger.debug('Cars with sorted components')
    # print(cars_service.get_cars_with_sorted_components())
    #
    # logger.debug('Component and cars with it')
    # print(cars_service.get_dict_component_and_cars())
    #
    # logger.debug('Cars with price between 121 and 200')
    # print(cars_service.get_cars_with_price_between(Decimal('121'), Decimal('200')))
    #
    # logger.warning('ENDING APP')


