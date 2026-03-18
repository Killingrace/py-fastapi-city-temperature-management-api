from asyncio import run
from sqlalchemy.exc import IntegrityError, OperationalError
from db.create_database import create_tables, insert_data, drop_tables


async def initialize_db():
    ask = input("Drop all created tables? [y/n]").lower()
    if ask == "y":
        await drop_tables()
    ask = input("Create tables? [y/n]").lower()
    if ask == "y":
        await create_tables()
    ask = input("insert data into tables? [y/n]").lower()    
    if ask == "y":    
        try:
            await insert_data()
        except IntegrityError:
            print("Data already inserted!")
        except OperationalError:
            print("Tables doesnt created!")

run(initialize_db())