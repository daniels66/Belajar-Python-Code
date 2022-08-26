# pengkondisian dalam python
'''
if kondisi:
    aksi
elif kondisi:
    aksi
elif kondisi:
    aksi
else:
    aksi default
'''

nilai = int(input("Masukkan nilai pelajaran anda = "))
int = 1
if type(nilai) == type(int):
    if nilai >= 90:
        print(f"Predikat anda  A untuk nilai {nilai}") 
    elif nilai >= 80:
        print(f"Predikat anda  B untuk nilai {nilai}")
    elif nilai >= 60:
        print(f"Predikat anda  C untuk nilai {nilai}")
    elif nilai >= 40:
        print(f"Predikat anda  D untuk nilai {nilai}")
    elif nilai < 40:
        print(f"Predikat anda E untuk nilai {nilai}")
else:
    print("Anda Salah Memasukkan Nilai")
