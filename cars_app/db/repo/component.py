from .crud import CrudRepo
from ..model.component import Component


class ComponentRepo(CrudRepo):
    def __init__(self, connection_pool):
        super().__init__(connection_pool, Component)
