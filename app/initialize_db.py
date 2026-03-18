from asyncio import run
from db.create_database import create_tables, insert_data


async def initialize_db():
    await create_tables()
    await insert_data()

run(initialize_db())