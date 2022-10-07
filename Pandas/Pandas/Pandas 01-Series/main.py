import pandas as pd

"""
series dalam pandas seperti kolom pada tabel
yang termasuk dalam satu dimensi array yang menerima berbagai tipe data
"""

x = ["a", "b", "c"]
var = pd.Series(x)
print(var, "\n")

x = [3, 2, 1]
var = pd.Series(x)
print(var, "\n")

x = [True, False, True]
var = pd.Series(x)
print(var, "\n")

x = [True, False, True]
var = pd.Series(x)
print(var[0], "\n")  # mengambil nilai berdasarkan index

"""
secara default index dalam pandas mulai dari nomor 0
apabila ingin custom index dilakukan cara dibawah
"""
x = ["a", "b", "c"]
var = pd.Series(x, index=["huruf_1", "huruf_2", "huruf_3"])
print(var, "\n")

x = ["a", "b", "c"]
var = pd.Series(x, index=["huruf_1", "huruf_2", "huruf_3"])
print(var["huruf_1"], "\n")  # mengambil nilai berdasarkan index key

"""
series dengan tipe data dictionary
"""
day = {
    "day_1": "senin",
    "day_2": "selasa",
    "day_3": "rabu",
    "day_4": "kamis",
    "day_5": "jumat",
    "day_6": "sabtu",
    "day_7": "minggu",
}

week = pd.Series(day)
print(week, "\n")

week = pd.Series(day, index=["day_1", "day_7"])  # hanya print bedasarkan key index
print(week, "\n")
