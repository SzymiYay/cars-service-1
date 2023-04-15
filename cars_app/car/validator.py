from .model import Color
from ..logger.model import MyLogger

from typing import Any, Callable
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import re


@dataclass
class Validator(ABC):
    # errors: dict[str, Any] = field(default_factory=dict)
    errors = None

    @abstractmethod
    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError

    def errors_to_str(self) -> str:
        return f"{', '.join([f'{key}: {message}' for key, message in self.errors.items()])}"

    @staticmethod
    def matches_regex(regex: str, text: str) -> bool:
        return re.match(regex, text) is not None

    @staticmethod
    def has_only_upper(text: str) -> bool:
        return Validator.matches_regex(r'^([A-Z]+\s?)+$', text)

    # @staticmethod
    # def validate_key_value(key: str, data: dict[str, Any], value_condition_fn: Callable[[str], bool]) -> list[str]:
    #     if key not in data:
    #         return ['Required']
    #
    #     if not value_condition_fn(data[key]):
    #         return ['Not correct']
    #
    #     return []


class CarValidator(Validator):

    def __init__(self):
        super().__init__()

    # def validate(self, data: dict[str, Any]) -> bool:
    #     model_val_res = self.validate_key_value('model', data, lambda model: self.has_only_upper(model))
    #
    #     if len(model_val_res) > 0:
    #         self.errors['model'] = model_val_res
    #
    #     return True

    def validate(self, car_data: dict[str, Any]) -> bool:
        self.errors = {
            'car': car_data['model'],
            'model': self._validate_car_model(car_data),
            'price': self._validate_car_price(car_data),
            'color': self._validate_car_color(car_data),
            'mileage': self._validate_car_mileage(car_data),
            'components': self._validate_car_components(car_data)
        }


        logger_validator = MyLogger.get_logger()

        if len(self.errors['model']) != 0 or \
                len(self.errors['price']) != 0 or \
                len(self.errors['color']) != 0:
            logger_validator.error(', '.join([f'{k}: {v}' for k, v in self.errors.items()]))
            return False

        return True

    def _validate_car_model(self, car_data: dict[str, Any]) -> list[str]:
        if 'model' not in car_data:
            return ['Required']

        errors = []
        car_model = car_data['model']

        if not self.has_only_upper(car_model):
            errors.append('Must contain only uppercase letters')

        return errors

    def _validate_car_price(self, car_data: dict[str, Any]) -> list[str]:
        if 'price' not in car_data:
            return ['Required']

        errors = []
        car_price = car_data['price']

        if not self.matches_regex(r'^\d+(\.\d+)?$', str(car_price)):
            errors.append('Must be decimal value')

        if car_price < 0:
            errors.append('Must be greater than zero')

        return errors

    def _validate_car_color(self, car_data: dict[str, Any]) -> list[str]:
        if 'color' not in car_data:
            return ['Required']

        errors = []
        car_color = car_data['color']

        colors = [color.name for color in Color]

        if car_color not in colors:
            errors.append(f'Permitted colors: {", ".join(colors)}')

        return errors

    def _validate_car_mileage(self, car_data: dict[str, Any]) -> list[str]:
        if 'mileage' not in car_data:
            return ['Required']

        errors = []
        car_mileage = car_data['mileage']

        if car_mileage < 0:
            errors.append('Must be greater than zero')

        return errors

    def _validate_car_components(self, car_data: dict[str, Any]) -> list[str]:
        if 'components' not in car_data:
            return ['Required']

        errors = []
        car_components = car_data['components']

        if len(car_components) == 0:
            errors.append('Must contain at least one element')

        for component in car_components:
            if not self.matches_regex(r'^([A-Z]+\s?)+$', component):
                errors.append('Must contain only uppercase letters')

        return errors
