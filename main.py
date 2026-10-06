import os
from sqlalchemy.orm import sessionmaker
from models.create_db import engine, Users, Dogs, db, make_tables
from models.errors import handle_db_error

Session = sessionmaker(bind=engine) # Настраивает подключение к нашей БД
session = Session() # Делает подключение к нашей БД для изменения, добавления или чтения данных

@handle_db_error
def create_data() -> None:
    print("Create new users")
    new_users = Users(name="Bob", score=500), Users(name="Alice", score=230), Users(name="Kuroko", score=610) # Новые юзеры
    session.add_all(new_users) # Добавляет новых юзеров в таблицу
    print("Done!")

    print("Create new dogs")
    new_dogs = Dogs(name="Sharick", age=5, breed="Bulldog", name="Bobik", age=10, breed="isn't dog") # Добавляем новых собак
    session.add(new_dogs) # Добавляем собаку в таблицу
    session.commit() # Сохраняет все изменения в БД
    print("Done!")

@handle_db_error
def show_data() -> None:
    print("Check all users")
    all_users = session.query(Users).all() # Выбрать всех юзеров
    for guy in all_users:
        print(f"ID: {guy.id} | Name: {guy.name} | Score: {guy.score}") # Кидаем инфу из таблицы про юзеров
    
    print("Check all dogs")
    all_dogs = session.query(Dogs).all() # Выбрать всех собак
    for dog in all_dogs:
        print(f"ID: {dog.id} | Name: {dog.name} | Age: {dog.age} | Breed: {dog.breed}") # Кидаем инфу из таблицы про собак

@handle_db_error
def main() -> None:
    print("Check DB") # Чекаем на наличие БД
    if not os.path.exists(db):
        print(f"{db} is not found! Creating {db}")
        make_tables()  # Создаем базу, если её нет
    else:
        print(f"{db} is found!")

    create_data()
    show_data()

if __name__ == "__main__":
    main()
