# latihan CRUD(create, read, update, delate)
# 1. menambah data siswa
# 2. menampilkan data siswa
# 3. ubah data siswa
# 4. hapus data siswa
# 5. pilihan tidak ditemukan

import os
import datetime
from time import strftime
import string
import random

template_siswa = {
    "nama": "nama",
    "almt": "almt",
    "tmp": "tmp",
    "tgl": datetime.datetime(1111, 1, 11),
}

data_siswa = {}

siswa = dict.fromkeys(
    template_siswa.keys()
)  # membuat key dalam dictionary menjadi kosong

# tampilan path dalam terminal
def path_terminal():
    # os.system = "cls" # windows
    os.system = "clear"  # linuc/mac


# membuat key random
def key_random():
    key = "".join(random.choice(string.digits) for i in range(5))
    return key


# Header
def header():
    print(55 * "-")
    print(f"SELAMAT DATANG".center(55))
    print(f"DIDALAM DATABASE SISWA".center(55))
    print(55 * "-")


# input user
def input_user():
    try:
        path_terminal()
        print("Anda Dapat Melakukan (1-4):")
        print("1. Menambahkan Data Siswa")
        print("2. Menampilkan Data Siswa")
        print("3. Mengubah Data Siswa")
        print("4. Menghapus Data Siswa")
        print("5. Selesai")
        pilihan = int(input("Pilihan Anda? = "))
        kondisi_inputuser(pilihan)
    except ValueError:
        header_eror()
        input_user()


# header tambah siswa
def header_tambahsiswa():
    print(55 * "-")
    print(f"MENAMBAHKAN DATA SISWA".center(55))
    print(55 * "-")


# header tampil siswa
def header_tampilsiswa():
    print(55 * "-")
    print(f"MENAMPILKAN DATA SISWA".center(55))
    print(f"{'Key':<6} {'Nama':<8} {'Alamat':<10} {'Tempat Lahir':<14} {'TTL':<10}")
    print(55 * "-")


# header ubah siswa
def header_ubahsiswa():
    print(55 * "-")
    print(f"MENGUBAH DATA SISWA".center(55))
    print(55 * "-")


# header hapus siswa
def header_hapussiswa():
    print(55 * "-")
    print(f"MENGHAPUS DATA SISWA".center(55))
    print(55 * "-")


# header selesai siswa
def header_selesai():
    print(55 * "-")
    print(f"TERIMA KASIH :)".center(55))
    print(55 * "-")


# header eror
def header_eror():
    print(55 * "-")
    print("Masukkan Angka (1-5) !!!")
    print(55 * "-")


# tambah siswa
def tambah_siswa(siswa):
    siswa["nama"] = input(f"Masukkan Nama Anda".ljust(35) + " = ")
    siswa["almt"] = input(f"Masukkan Alamat Anda".ljust(35) + " = ")
    siswa["tmp"] = input(f"Masukkan Tempat Lahir Anda".ljust(35) + " = ")
    # tanggal = int(input("Masukkan Tanggal Lahir Anda (1-31)".ljust(35) + " = "))
    # bulan = int(input("Masukkan Bulan Lahir Anda (1-12)".ljust(35) + " = "))
    # tahun = int(input("Masukkan Tahun Lahir Anda".ljust(35) + " = "))
    # siswa["tgl"] = datetime.datetime(tahun, bulan, tanggal)
    print(55 * "-")
    tambah_lagi()


# tampil siswa
def tampil_siswa(data_siswa):
    for id in data_siswa:
        key = id
        nama = data_siswa[key]["nama"]
        almt = data_siswa[key]["almt"]
        tmp = data_siswa[key]["tmp"]
        tgl = data_siswa[key]["tgl"].strftime("%x")
        print(f"{key:<6} {nama:<8} {almt:<10} {tmp:<14} {tgl:<10}")
    print("\n")


# tambah lagi
def tambah_lagi():
    try:
        tambah = input("Menambahkan Data Lagi (y/n)?? ")
        tambah.lower()
        print(55 * "-")
        if tambah == "y":
            tambah_siswa(siswa)
        elif tambah == "n":
            print(55 * "-")
            input_user()
    except:
        print("Masukkan (y/n)!!!")


# kondisi input user
def kondisi_inputuser(angka):
    if angka == 1:
        header_tambahsiswa()
        tambah_siswa(siswa)
        data_siswa.update({key_random(): siswa})
    elif angka == 2:
        header_tampilsiswa()
    elif angka == 3:
        header_ubahsiswa()
    elif angka == 4:
        header_hapussiswa()
    elif angka == 5:
        header_selesai()
    else:
        header_eror()


# Program Utama
header()
input_user()
