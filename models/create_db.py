from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from models.errors import handle_db_error

db = "base.db"

engine = create_engine(f"sqlite:///{db}") # Создаю бд на SQLite

base = declarative_base() # Делает классы ниже - таблицами

class Users(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

class Dogs(base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    breed = Column(String)

@handle_db_error
def make_tables():
    base.metadata.create_all(engine)
    print("DB is maked.")

