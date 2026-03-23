from db.create_database import create_tables, insert_data, drop_tables


async def initialize_db():
    await drop_tables()
    await create_tables()
    await insert_data()
