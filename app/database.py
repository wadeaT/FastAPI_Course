from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import settings
"""
This file is essentially your Database Configuration Center.
It sets up the rules for how your app will talk to PostgreSQL.
"""

#remember to change this in the future! before putting it in git! 
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345password@localhost/fastapi'
#SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg://postgres:12345password@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

# url = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'


"""
The engine is the core physical connection manager between
Python and the database (using psycopg under the hood)
"""
#engine is what responsible for SQLalchemy to connect to postgres database
engine = create_engine(SQLALCHEMY_DATABASE_URL) # what happens if I add (..., echo= True)

"""
This is a factory that creates individual database "sessions."
 A session is a temporary workspace for a specific database transaction.
 """
#if we want to talk to the database we need a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This creates a base Python class
Base = declarative_base()

#What it is: A function that provides a database session to your route,
#  and ensures it closes properly
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



"""
import psycopg
from psycopg.rows import dict_row
import time

while True:

    try: 
        conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres',
                            password='12345password', row_factory=dict_row)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error: ", error)
        time.sleep(2)

"""