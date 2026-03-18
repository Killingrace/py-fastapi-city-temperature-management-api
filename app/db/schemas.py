from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CityAddDTO(BaseDTO):
    name: str
    additional_info: str


class CityDTO(CityAddDTO):
    id: int


class CityRelDTO(CityDTO):
    temperature: Optional["TemperatureDTO"] = None


class TemperatureAddDTO(BaseDTO):
    city_id: int
    


class TemperatureDTO(TemperatureAddDTO):
    id: int
    date_time: datetime
    temperature: float | None


class TemperatureRelDTO(TemperatureDTO):
    city: "CityDTO"
