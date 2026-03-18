import asyncio
import uvicorn

from fastapi import FastAPI

from routers.cities import cities_router
from routers.temperatures import temperatures_router
from db.create_database import create_tables, insert_data


app = FastAPI()
app.include_router(cities_router)
app.include_router(temperatures_router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080)
