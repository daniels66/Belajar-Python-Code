import pandas as pd
from numpy import random

data = pd.DataFrame(random.randint(1, 10, size=(5, 10)))

"""
prefik digunakan untuk memberikan nama bagian depan pada kolom data frame
"""
print(data.add_prefix("kolom_"), "\n")
print(data.add_suffix("_kolom"), "\n")
