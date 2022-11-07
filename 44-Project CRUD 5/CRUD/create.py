from database import database
from database.data import data


def tambah_data():
    try:
        with open(database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data())
    except Exception as error_massage:
        print(error_massage)
