# Latihan mengambil data dan waktu

import datetime as dt
from re import A

print("Masukkan tanggal lahir anda :\n")
hari = int(input("Hari = "))
bulan = int(input("Bulan = "))
tahun = int(input("Tahun = "))
tanggal_lahir = dt.date(tahun,bulan,hari)
print("Tanggal Lahir Anda = ", tanggal_lahir)

today = dt.date.today()
umur_hari = today-tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365)//30
print(f"Hari ini adalah hari = {today:%A}")
print(f"Umur anda adalah {umur_tahun} tahun, {umur_bulan} bulan")