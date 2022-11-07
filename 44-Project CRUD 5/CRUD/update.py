from .read import read
import database
import datetime


def ubah_data():
    print("-" * 55)
    while True:
        no_siswa = int(input("Masukkan Nomor Yang Ingin Anda Ubah = "))
        data_siswa = read(index=no_siswa)
        if data_siswa:
            break
        else:
            print("-" * 55)
            print("Nomor Tidak Ditemukan !!!")
            print("-" * 55)

    print("-" * 55)
    data_split = data_siswa.split(",")
    key = data_split[0]
    nama = data_split[1]
    almt = data_split[2]
    tmp = data_split[3]
    tgl = data_split[4][:-1]

    while True:
        print("Pilih Data Yang Ingin Diubah (1-4)")
        print("1. Nama\t\t\t=", nama)
        print("2. Alamat\t\t=", almt)
        print("3. Tempat Lahir\t\t=", tmp)
        print("4. Tanggal Lahir\t=", tgl)
        pilihan = int(input("Pilihan Anda ? "))
        print("-" * 55)

        match pilihan:
            case 1:
                nama = input(f"Masukkan Nama Baru".ljust(35) + " = ")
            case 2:
                almt = input(f"Masukkan Alamat Baru".ljust(35) + " = ")
            case 3:
                tmp = input(f"Masukkan Tempat Lahir Anda".ljust(35) + " = ")
            case 4:
                tanggal = int(
                    input("Masukkan Tanggal Lahir Anda (1-31)".ljust(35) + " = ")
                )
                bulan = int(input("Masukkan Bulan Lahir Anda (1-12)".ljust(35) + " = "))
                tahun = int(input("Masukkan Tahun Lahir Anda".ljust(35) + " = "))
                tgl = datetime.date(tahun, bulan, tanggal)

        print("-" * 55)
        print("Data Baru")
        print("1. Nama\t\t\t=", nama)
        print("2. Alamat\t\t=", almt)
        print("3. Tempat Lahir\t\t=", tmp)
        print("4. Tanggal Lahir\t=", tgl)
        print("-" * 55)

        sesuai = input("Apakah Data Sudah Sesuai (y/n)? ")
        sesuai.lower()
        if sesuai == "y":
            print("-" * 55)
            break
        elif sesuai == "n":
            print("-" * 55)
        else:
            True

    update(no_siswa, key, nama, almt, tmp, tgl)


def update(no_siswa, key, nama, almt, tmp, tgl):
    data = database.TEMPLATE_SISWA.copy()
    data["pk"] = key
    data["nama"] = nama + database.TEMPLATE_SISWA["nama"][len(nama) :]
    data["almt"] = almt + database.TEMPLATE_SISWA["almt"][len(almt) :]
    data["tmp"] = tmp + database.TEMPLATE_SISWA["tmp"][len(tmp) :]
    data["tgl"] = str(tgl)

    data_str = (
        f'\n{data["pk"]},{data["nama"]},{data["almt"]},{data["tmp"]},{data["tgl"]}\n'
    )

    panjang_data = len(data_str)
    try:
        with (open(database.DB_NAME, "r+")) as file:
            file.seek(panjang_data * (no_siswa - 1))
            file.write(data_str)
    except Exception as error_massage:
        print(error_massage)
