from .crud import CrudRepo
from ..model.car import Car


class CarRepo(CrudRepo):
    def __init__(self, connection_pool):
        super().__init__(connection_pool, Car)
