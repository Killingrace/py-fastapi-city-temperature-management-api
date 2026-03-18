import requests
from db.config import settings


async def get_temperature(city_name: str) -> float | None:
    location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={settings.API_KEY}").json()
    try:
        location_lat = location[0]["lat"]
        location_lon = location[0]["lon"]
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&appid={settings.API_KEY}").json()
        return round(weather["main"]["temp"] - 273.15, 1)
    except IndexError:
        return None
