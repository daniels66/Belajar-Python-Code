# sorting array pada numpy
import numpy as np

# membuat matrix randon
a = np.floor(np.random.randn(2, 3) * 10)
print(a)

# max,mix,argmax,argmin
print("max,mix,argmax,argmin".center(30, "-"))
print(f"nilai max dari a = {a.max()}")
print(f"nilai min dari a = {a.min()}")
print(f"nilai max berada pada index = {a.argmax()}")
print(f"nilai min berada pada index = {a.argmin()}")

# mengurutkan nilai
print("sort nilai".center(30, "-"))
print(f"nilai sebelum diurutkan dari a = \n{a}")
print(f"nilai setelah diurutkan dari a = \n{np.sort(a)}")
"""
untuk sort diurutkan pada masing masing kolom dengan 
nilai terbesar berada disebelah kanan,
nilai terkecil berada di sebelah kiri,

apabila mengurutkan string maka,
abjad awal akan berada di sebelah kiri,
abjad akhir akan berada di sebelah kanan,

apabila mengurutkan boolean maka,
false akan didahulukan, kemudian true
"""
print(f"nilai setelah diurutkan dari a = \n{np.argsort(a)}")

print("sort multi type array".center(30, "-"))
type = [
    ("nama", "S100"),
    ("tinggi_bdn", int),
]  # s100 adalah nilai string dengan nilai maximal 100 char
data = [("daniel", 168), ("bili", 164), ("alil", 160)]

print(f"data = {data}")
h = np.array(data, dtype=type)

print(f"sort dengan tinggi badan")
print(np.sort(h, order="tinggi_bdn"))
print(f"sort dengan nama")
print(np.sort(h, order="nama"))

# mencari nilai
# menggunakan where() dan searchsort()
print("search nilai".center(30, "-"))
b = np.array([1, 2, 3, 4, 5, 7, 8, 9, 8, 7, 7])
print(b)

# where(array == <apa yang dicari>)
b_where = np.where(
    b == 7
)  # akan menghasilkan semua index dimana nilai tersebut disimpan dalam array
print(b_where)
b_where = np.where(b == 6)  # tidak akan ada nilai index yang ditampilkan dalam array
print(b_where)

# searchsorted(array , nilai, sisi)
b_srcst = np.searchsorted(
    b, 7
)  # akan menghasilkan index awal dimana nilai tersebut disimpan dalam array
print("nilai 7 berada pada index ", b_srcst, "dari kiri")
b_srcst = np.searchsorted(b, 7, side="right")
print("nilai 7 berada pada index ", b_srcst, "dari kanan")
