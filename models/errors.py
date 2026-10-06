import sys
from sqlalchemy.exc import SQLAlchemyError

def handle_db_error(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            print("[  ERROR  ] Произошёл сбой в работе SQLAlchemy!")
            print(f"Лог ошибки: {e}")
        sys.exit(1)
    return wrapped
