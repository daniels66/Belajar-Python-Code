# latihan dictionary
import datetime
from time import strftime
import os
import string
import random

template_siswa = {
    'nama':'nama',
    'almt':'almt',
    'tmp':'tmp',
    'tgl':datetime.datetime(1111,1,11),
}

data_siswa = {}

# Header
def header():
    print(55*"-")
    print(f"INPUT".center(55))
    print(f"DATA SISWA".center(55))
    print(55*"-")

# membuat key kosong
def key_kosong():
    pass

# input siswa
def input_siswa(siswa):
    siswa['nama'] = input(f"Masukkan Nama Anda".ljust(35)+" = ")
    siswa['almt'] = input(f"Masukkan Alamat Anda".ljust(35)+" = ")
    siswa['tmp'] = input(f"Masukkan Tempat Lahir Anda".ljust(35)+" = ")
    tanggal = int(input("Masukkan Tanggal Lahir Anda (1-31)".ljust(35)+" = "))
    bulan = int(input("Masukkan Bulan Lahir Anda (1-12)".ljust(35)+" = "))
    tahun = int(input("Masukkan Tahun Lahir Anda".ljust(35)+" = "))
    siswa['tgl'] = datetime.datetime(tahun,bulan,tanggal)

# tampilan path dalam terminal
def path_terminal():
    # os.system = "cls" # windows
    os.system = "clear" # linuc/mac

# membuat key random
def key_random():
    key = ''.join(random.choice(string.digits) for i in range(5))
    return key

# Header input nama
def header_input_nama():
    print(55*"-")
    print(f"{'Key':<6} {'Nama':<8} {'Alamat':<10} {'Tempat Lahir':<14} {'TTL':<10}")
    print(55*"-")

# looping siswa
def looping_siswa(data_siswa):
    for id in data_siswa:
        key = id
        nama = data_siswa[key]['nama']
        almt = data_siswa[key]['almt']
        tmp = data_siswa[key]['tmp']
        tgl = data_siswa[key]['tgl'].strftime("%x")
        print(f"{key:<6} {nama:<8} {almt:<10} {tmp:<14} {tgl:<10}")
    print("\n")


# lanjut ga??
def lanjut():
    while True:
        lanjut = input("lanjut (y/n)? : ")
        lanjut.lower()
        if lanjut == 'n':
            break
        elif lanjut == 'y':
            break
        else:
            print("Masukkan (y/n)!!!")
            True
    print(55*"-")
    return lanjut

# Header
header()
while True:
    siswa = dict.fromkeys(template_siswa.keys()) # membuat key dalam dictionary menjadi kosong

    # tampilan path dalam terminal
    path_terminal()

    # input siswa
    input_siswa(siswa)
    
    # update data dan membuat key random
    data_siswa.update({key_random():siswa})

    # Header input nama
    header_input_nama()

    # Looping data siswa
    looping_siswa(data_siswa)

    # lanjut ga??
    if lanjut() == 'n':
        break

print(f"Terima Kasih :)")
