from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from tools.tools import DataBase
from routers.cities import CityDoesntExistError
from db import crud
from db.schemas import TemperatureRelDTO

temperatures_router = APIRouter()
NoTemperatureError = HTTPException(status_code=404, detail="No temperatures fethed!")

@temperatures_router.post("/temperatures/update", status_code=status.HTTP_201_CREATED)
async def fetch_all_temperatures(
    db: DataBase,
):
    cities = await crud.select_all_cities(db=db)
    await crud.validate_all_temperatures(db=db, cities=cities)
    return


@temperatures_router.get("/temperatures", response_model=list[TemperatureRelDTO])
async def get_temperature_by_id(
    db: DataBase,
    city_id: int | None = None
):
    if city_id:
        city = await crud.select_city_by_id(db=db, city_id=city_id)
        if not city:
            raise CityDoesntExistError
        
        if not city.temperature:
            raise NoTemperatureError
        
        return await crud.select_temperature_by_city_id(db=db, city_id=city_id)
    else:
        temperatures = await crud.select_all_temperatures(db=db)
        return temperatures
