# merubah tipe data dalam pyhton

print("====INTEGER====")
nilai_int = 10
print("nilai variable = ", nilai_int)
print("type variable = ", type(nilai_int))

nilai_float = float(nilai_int)
print("nilai variable = ", nilai_float)
print("type variable = ", type(nilai_float))

nilai_string = str(nilai_int)
print("nilai variable = ", nilai_string)
print("type variable = ", type(nilai_string)) # dikonversi dari int menjadi string

nilai_bool = bool(nilai_int)
print("nilai variable = ", nilai_bool)
print("type variable = ", type(nilai_bool)) # apabila int bernilai 0 maka akan bernilai false

print("\n\n")

print("====FLOAT====")
nilai_float = 10.6
print("nilai variable = ", nilai_float)
print("type variable = ", type(nilai_float))

nilai_int = int(nilai_int)
print("nilai variable = ", nilai_int)
print("type variable = ", type(nilai_int)) # dibulatkan kebawah

nilai_string = str(nilai_float)
print("nilai variable = ", nilai_string)
print("type variable = ", type(nilai_string)) # dikonversi dari float menjadi string

nilai_bool = bool(nilai_float)
print("nilai variable = ", nilai_bool)
print("type variable = ", type(nilai_bool)) # apabila int bernilai 0 maka akan bernilai false

print("\n\n")

print("====STRING====")
nilai_string = "daniels"
print("nilai variable = ", nilai_string)
print("type variable = ", type(nilai_string))

''' 
nilai_int = int(nilai_string)
print("nilai variable = ", nilai_int)
print("type variable = ", type(nilai_int)) # tidak dapat mengubah string menjadi int

nilai_float = float(nilai_string)
print("nilai variable = ", nilai_float)
print("type variable = ", type(nilai_float)) # tidak dapat mengubah string menjadi float
'''
nilai_bool = bool(nilai_string)
print("nilai variable = ", nilai_bool)
print("type variable = ", type(nilai_bool)) # apabila string tidak terdapat variable maka akan false

print("\n\n")

print("====BOOLEAN====")
nilai_bool = False
print("nilai variable = ", nilai_bool)
print("type variable = ", type(nilai_bool))

nilai_int = int(nilai_bool)
print("nilai variable = ", nilai_int)
print("type variable = ", type(nilai_int)) # apabila bernilai true akan berangka 1

nilai_float = float(nilai_bool)
print("nilai variable = ", nilai_float)
print("type variable = ", type(nilai_float)) # apabila bernilai true akan berangka 1.0


nilai_string = str(nilai_bool)
print("nilai variable = ", nilai_string)
print("type variable = ", type(nilai_string)) # merubah menjadi string true or false

print("\n\n")