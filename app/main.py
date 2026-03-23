import os
from initialize_db import initialize_db
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.cities import cities_router
from routers.temperatures import temperatures_router


app = FastAPI()
app.include_router(cities_router)
app.include_router(temperatures_router)


@app.get("/", response_class=HTMLResponse)
async def hello():
    return """<h1>Hello!</h1>
<p>Read the Swagger documentation on /docs path</p>"""

if __name__ == "__main__":
    if os.getenv("DEBUG", "False") == "True":
        if not os.path.exists(os.getenv("DATABASE_URL", "None")):
            asyncio.run(initialize_db())
        uvicorn.run("main:app", host="0.0.0.0", port=8080)
    else:
        uvicorn.run("main:app", host="localhost", port=8080)