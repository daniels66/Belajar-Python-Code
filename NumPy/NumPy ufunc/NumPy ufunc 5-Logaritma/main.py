# operasi logaritma dalam numpy
"""
log2()
log10()
log dengan input terserah
"""
from math import log
import numpy as np


arr = np.arange(1, 10)
print(f"\nlog2 setiap index array =\n{np.log2(arr)}")
print(f"\nlog10 setiap index array =\n{np.log10(arr)}")  # default log
"""
log dengan input terserah
import log dari package math, masukkan kedalam function pribadi dengan
input(2 buah argument) dan output (hasil log)
"""
nplog = np.frompyfunc(log, 2, 1)
print("\nlogx(x) log dengan nilai x bebas\n")
print(nplog(100, 15))  # log15(100) log 15 dengan nilai input 100
