import datetime
from . import data

DB_NAME = "data.txt"
TEMPLATE_SISWA = {
    "nama": "nama",
    "almt": "almt",
    "tmp": "tmp",
    "tgl": datetime.date(1111, 1, 11),
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            pass
    except:
        print("Database Tidak Ditemukan".center(55))
        print("Silahkan Membuat Database Awal Terlebih Dahulu".center(55), "\n")
        data.create_first_data()
