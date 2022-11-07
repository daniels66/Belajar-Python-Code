import datetime
import random
import string
from database import database


def data():
    nama = input(f"Masukkan Nama Anda".ljust(35) + " = ")
    almt = input(f"Masukkan Alamat Anda".ljust(35) + " = ")
    tmp = input(f"Masukkan Tempat Lahir Anda".ljust(35) + " = ")
    tanggal = int(input("Masukkan Tanggal Lahir Anda (1-31)".ljust(35) + " = "))
    bulan = int(input("Masukkan Bulan Lahir Anda (1-12)".ljust(35) + " = "))
    tahun = int(input("Masukkan Tahun Lahir Anda".ljust(35) + " = "))
    tgl = datetime.date(tahun, bulan, tanggal)

    data = database.TEMPLATE_SISWA.copy()

    data["pk"] = random_string(6)
    data["nama"] = nama + database.TEMPLATE_SISWA["nama"][len(nama) :]
    data["almt"] = almt + database.TEMPLATE_SISWA["almt"][len(almt) :]
    data["tmp"] = tmp + database.TEMPLATE_SISWA["tmp"][len(tmp) :]
    data["tgl"] = str(tgl)

    data_str = (
        f'{data["pk"]},{data["nama"]},{data["almt"]},{data["tmp"]},{data["tgl"]}\n'
    )

    return data_str


def create_first_data():
    try:
        with open(database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data())
    except Exception as error_massage:
        print(error_massage)


def random_string(panjang: int) -> str:
    hasil_string = "".join(random.choice(string.digits) for i in range(panjang))
    return hasil_string
