import datetime
from database import database
from database import random_string


def tambah_data():
    nama = input(f"Masukkan Nama Anda".ljust(35) + " = ")
    almt = input(f"Masukkan Alamat Anda".ljust(35) + " = ")
    tmp = input(f"Masukkan Tempat Lahir Anda".ljust(35) + " = ")
    tanggal = int(input("Masukkan Tanggal Lahir Anda (1-31)".ljust(35) + " = "))
    bulan = int(input("Masukkan Bulan Lahir Anda (1-12)".ljust(35) + " = "))
    tahun = int(input("Masukkan Tahun Lahir Anda".ljust(35) + " = "))
    tgl = datetime.datetime(tahun, bulan, tanggal)

    data = database.TEMPLATE_SISWA.copy()

    data["pk"] = random_string(6)
    data["nama"] = nama
    data["almt"] = almt
    data["tmp"] = tmp
    data["tgl"] = tgl

    data_str = (
        f'{data["pk"]},{data["nama"]},{data["almt"]},{data["tmp"]},{data["tgl"]}\n'
    )

    try:
        with open(database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except Exception as error_massage:
        print(error_massage)
