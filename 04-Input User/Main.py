# cara mengambil input dari user

data_input = input("masukkan nama = ")
print("nama anda adalah = ",data_input)
print("\n tipe data = ", type(data_input))
# input memiliki kelemahan yaitu akan merubah data yang dimasukkan menjadi format string
# apabila menginginkan hasil input bernilai int atau float gunakan casting seperti tutorial sebelumnya

data_angka = float(input("masukkan angka = "))
print("angka yang anda masukkan adalah = ", data_angka)
print("\n tipe data = ", type(data_angka))