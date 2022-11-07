# latihan CRUD(create, read, update, delate)
# 1. menambah data siswa
# 2. menampilkan data siswa
# 3. ubah data siswa
# 4. hapus data siswa
# 5. pilihan tidak ditemukan

# Update Database

import os
import database
import CRUD
from header.header import (
    header,
    header_hapussiswa,
    header_selesai,
    header_tambahsiswa,
    header_tampilsiswa,
    header_ubahsiswa,
)

# input user
def input_user():
    print("Anda Dapat Melakukan (1-5):")
    print("1. Menampilkan Data Siswa")
    print("2. Menambahkan Data Siswa")
    print("3. Mengubah Data Siswa")
    print("4. Menghapus Data Siswa")
    print("5. Selesai", "\n")


# kondisi input user
def kondisi_inputuser(angka):
    match angka:
        case 1:
            header_tampilsiswa()
            CRUD.read_data()
        case 2:
            header_tambahsiswa()
            CRUD.tambah_data()
            header_tampilsiswa()
            CRUD.read_data()
        case 3:
            header_ubahsiswa()
            CRUD.read_data()
            CRUD.ubah_data()
            header_tampilsiswa()
            CRUD.read_data()
        case 4:
            header_hapussiswa()


if __name__ == "__main__":
    operasi_sistem = os.name

    match operasi_sistem:
        case "posix":
            os.system("clear")
        case "nt":
            os.system("cls")

    header()

    # cek database
    database.init_console()

    while True:
        match operasi_sistem:
            case "posix":
                os.system("clear")  # untuk mempercantik tampilan terminal di mac/linux
            case "nt":
                os.system("cls")  # untuk mempercantik tampilan terminal di windows

        header()
        input_user()
        pilihan = int(input("Pilihan Anda? = "))
        kondisi_inputuser(pilihan)

        if pilihan == 5:
            break

        print("-" * 55)
        selesai = input("Apakah Selesai (y/n)? = ")
        selesai.lower()
        if selesai == "y":
            break

    header_selesai()
