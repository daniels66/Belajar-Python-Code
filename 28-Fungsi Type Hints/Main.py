# fungsi dengan type hints
'''
type hinst digunakan dalam fungsi untuk membuat argument tertentu yang
dapat masuk kedalam fungsi tersebut
'''

from ast import arguments


def tambah(argument1:int,argument2:int):
    hasil = argument1 + argument2
    return hasil

print(tambah(3,5))
# print(tambah(kamu,5)) # akan erorr dikarenakan argument tidak bertipe yang telah ditentukan

'''
int tambah(int argument1, int argument2){
    hasil = argument1 + argument2
    return hasil
}
diatas seperti dalam c++

def tambah(argument1,argument2) -> int:
    hasil = argument1 + argument2
    return hasil
apabila ingin fungsi seperti c++ dalam pyhton
'''