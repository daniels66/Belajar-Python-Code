import pandas as pd
from numpy import random

data = pd.DataFrame(random.randint(1, 10, size=(5, 10)))

"""
prefik digunakan untuk memberikan nama bagian depan pada kolom data frame
"""
print(data, "\n")
kolom = 1
angka = 2
print("pada kolom ke ", kolom, "terdapat angka ", angka, " ??")
print(data[data[kolom] == angka])
