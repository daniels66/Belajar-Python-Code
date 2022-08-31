# nesting dictionary

import datetime
from time import strftime

siswa1 = {
    'nama':'Daniel',
    'almt':'Laban',
    'tmp':'Surabaya',
    'tgl':datetime.datetime(2002,4,28),
}
siswa2 = {
    'nama':'Bili',
    'almt':'Lakar',
    'tmp':'Gresik',
    'tgl':datetime.datetime(2001,6,6),
}
siswa3 = {
    'nama':'Alil',
    'almt':'Setro',
    'tmp':'Sidoarjo',
    'tgl':datetime.datetime(1999,8,26),
}
data_siswa = {
    'mhs1':siswa1,
    'mhs2':siswa2,
    'mhs3':siswa3,
}

print(f"data_siswa = \n{data_siswa}\n")
print(f"{'Key':<6} {'Nama':<8} {'Alamat':<10} {'Tempat Lahir':<14} {'TTL':<10}")
print(55*"-")

# Looping setiap item
for siswa in data_siswa:
    key = siswa
    nama = data_siswa[key]['nama']
    almt = data_siswa[key]['almt']
    tmp = data_siswa[key]['tmp']
    tgl = data_siswa[key]['tgl'].strftime("%x")
    
    print(f"{key:<6} {nama:<8} {almt:<10} {tmp:<14} {tgl:<10}")
print('\n')