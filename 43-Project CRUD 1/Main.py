# latihan CRUD(create, read, update, delate)
# 1. menambah data siswa
# 2. menampilkan data siswa
# 3. ubah data siswa
# 4. hapus data siswa
# 5. pilihan tidak ditemukan

import os
from header.header import (
    header,
    header_eror,
    header_hapussiswa,
    header_selesai,
    header_tambahsiswa,
    header_tampilsiswa,
    header_ubahsiswa,
)

# input user
def input_user():
    try:
        print("Anda Dapat Melakukan (1-5):")
        print("1. Menambahkan Data Siswa")
        print("2. Menampilkan Data Siswa")
        print("3. Mengubah Data Siswa")
        print("4. Menghapus Data Siswa")
        print("5. Selesai", "\n")
    except ValueError:
        header_eror()
        input_user()


# kondisi input user
def kondisi_inputuser(angka):
    match angka:
        case 1:
            header_tambahsiswa()
        case 2:
            header_tampilsiswa()
        case 3:
            header_ubahsiswa()
        case 4:
            header_hapussiswa()
        case 5:
            pass
        case _:
            header_eror()


if __name__ == "__main__":
    operasi_sistem = os.name

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

        print("\n")
        selesai = input("Apakah Selesai (y/n)? ")
        selesai.lower()
        if selesai == "y":
            break

    header_selesai()
