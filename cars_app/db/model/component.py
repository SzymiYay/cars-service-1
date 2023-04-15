from dataclasses import dataclass


@dataclass
class Component:
    id: int | None = None
    name: str | None = None
    car_id: int | None = None
