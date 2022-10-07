import pandas as pd

"""
DataFrame adalah 2 dimensi data struktur atau array 2 dimensi atau 
sebuah table dengan baris dan kolom
"""

identity = {
    "nama": ["daniel", "bili", "alil", "rama"],
    "umur": [20, 21, 20, 21],
    "status": [
        "single",
        "single",
        "single",
        "single",
    ],
}

data = pd.DataFrame(identity)
print(data, "\n")
print(data.loc[1], "\n")  # mengambil data satu index tertentu
print(data.loc[[1, 3, 1]], "\n")  # mengambil data pada beberapa index

"""
apabila ingin mengganti index pada DataFrame dapat digunakan cara pada series
"""
data = pd.DataFrame(identity, index=["Nomor1", "Nomor2", "Nomor3", "Nomor4"])
print(data, "\n")
print(data.loc["Nomor1"], "\n")  # mengambil data satu index tertentu
print(
    data.loc[["Nomor1", "Nomor3", "Nomor1"]], "\n"
)  # mengambil data pada beberapa index
