from ..validator.text import has_only_upper, matches_regex
from .model import Color
from ..logger.model import MyLogger

from typing import Any

def validate_car_data(car_data: dict[str, Any]) -> bool:
    errors = {
        'car': car_data['model'],
        'model': _validate_car_model(car_data),
        'price': _validate_car_price(car_data),
        'color': _validate_car_color(car_data)
    }

    logger_validator = MyLogger.get_logger()

    if len(errors['model']) != 0 or \
            len(errors['price']) != 0 or \
            len(errors['color']) != 0:
        logger_validator.error(', '.join([f'{k}: {v}' for k, v in errors.items()]))
        return False

    return True


def _validate_car_model(car_data: dict[str, Any]) -> list[str]:
    if 'model' not in car_data:
        return ['Required']

    errors = []
    car_model = car_data['model']

    if not has_only_upper(car_model):
        errors.append('Must contain only uppercase letters')

    return errors


def _validate_car_price(car_data: dict[str, Any]) -> list[str]:
    if 'price' not in car_data:
        return ['Required']

    errors = []
    car_price = car_data['price']

    if not matches_regex(r'^\d+(\.\d+)?$', str(car_price)):
        errors.append('Must be decimal value')

    if car_price < 0:
        errors.append('Must be greater than zero')

    return errors


def _validate_car_color(car_data: dict[str, Any]) -> list[str]:
    if 'color' not in car_data:
        return ['Required']

    errors = []
    car_color = car_data['color']

    if not hasattr(Color, car_color):
        errors.append(f'Permitted colors: {", ".join(Color._member_names_)}')

    return errors


def _validate_car_mileage(car_data: dict[str, Any]) -> list[str]:
    if 'mileage' not in car_data:
        return ['Required']

    errors = []
    car_mileage = car_data['mileage']

    if car_mileage < 0:
        errors.append('Must be greater than zero')

    return errors


def _validate_car_components(car_data: dict[str, Any]) -> list[str]:
    if 'components' not in car_data:
        return ['Required']

    errors = []
    car_components = car_data['components']

    if len(car_components) == 0:
        errors.append('Must contain at least one element')

    for component in car_components:
        if not matches_regex(r'^([A-Z]+\s?)+$', component):
            errors.append('Must contain only uppercase letters')

    return errors
