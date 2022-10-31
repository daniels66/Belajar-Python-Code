import database
from time import strftime

from database import data


def read():
    try:
        with open(database.DB_NAME, "r") as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False


def read_data():
    data_file = read()

    # Data
    for data in data_file:
        data_break = data.split(",")
        key = data_break[0]
        nama = data_break[1]
        almt = data_break[2]
        tmp = data_break[3]
        tgl_eror = data_break[4]
        tgl = tgl_eror[0:11]
        print(f"{key:<6} {nama:<8} {almt:<10} {tmp:<14} {tgl:<10}")
        # print(f"{key:<6} {nama:<8} {almt:<10} {tmp:<14}")
