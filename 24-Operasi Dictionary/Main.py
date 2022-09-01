# operasi pada dictionary
import datetime

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
    'ssw1':siswa1,
    'ssw2':siswa2,
    'ssw3':siswa3,
}

# menghitung panjang dari dictionary
p_ds = len(data_siswa)
print(f"Panjang Data Siswa = {p_ds}")
p_ds = len(data_siswa['ssw1'])
print(f"Panjang Data Siswa pada Siswa1 = {p_ds}")

# mengecek key ada atau tidak
key = 'tmp'
check_key = key in siswa1
print(f"key ({key}) ada dalam siswa1 ? {check_key}")

# mengambil nilai dengan key pada dictionary
key = 'nama'
print(f"{siswa1[key]}")
key = 'lls'
# print(f"{siswa1[key]}") # akan eror
'''
apabila nilai di dalam dictionary tidak ada
jika tidak memakai gate akan dianggap eror
jika memakai get akan ditambilkan none atau diberi pesan tertentu
'''
print(f"{siswa1.get('tmp')}") 
key = 'ttl'
message = "key tidak ditemukan"
print(f"{siswa1.get(key,message)}")

# update data dalam dictionary
print(f"siswa1 sebelum dirubah = \n{siswa1}")
siswa1['nama'] = 'Rama'
print(f"siswa1 setelah dirubah = \n{siswa1}")
siswa1['lls'] = True
print(f"siswa1 setelah ditambah = \n{siswa1}")
'''
selain menggunakan cara diatas untuk update data
dapat menggunakan update()
'''
siswa1.update({"nim":352513})
print(f"siswa1 setelah update = \n{siswa1}")

# delete data
del siswa1['lls']
print(f"siswa1 setelah didelete = \n{siswa1}")

