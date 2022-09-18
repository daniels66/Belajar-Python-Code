# pengenalan LCM dan GDC
"""
LCM = Lowest Common Number
GDC = Greates Common Denominator
"""

import numpy as np

num1 = 4
num2 = 6
arr = np.array([3, 6, 9])
arng = np.arange(1, 11, 3)

print(f"number1 = {num1}, number2 = {num2}")
print(f"array = {arr}")
print(f"arange = {arng}")

print("Lowest Common Number (LCM)".center(40, "-"))


x = np.lcm(num1, num2)
print(x)
"""
hasil perkalian paling rendah masing masing nomor dengan hasil yang sama adalah 12
4*3 = [12]
6*2 = [12]
"""

x = np.lcm.reduce(arr)
print(x)
"""
hasil perkalian paling rendah masing masing array dengan hasil yang sama adalah 18
3*6 = [18]
6*3 = [18]
9*2 = [18]
"""

x = np.lcm.reduce(arng)
print(x)
"""
hasil perkalian paling rendah masing masing arange dengan hasil yang sama adalah 140
1*140 = [140]
4*35  = [140]
7*20  = [140]
10*14 = [140]
"""

print("Greates Common Denominator (GCD)".center(40, "-"))


x = np.gcd(num1, num2)
print(x)
"""
pembagi masing masing nomor paling rendah adalah 2
4/[2] = 2
6/[2] = 3
"""

x = np.gcd.reduce(arr)
print(x)
"""
pembagi masing masing array paling rendah adalah 2
3/[3] = 0
6/[3] = 2
9/[3] = 3
"""

x = np.gcd.reduce(arng)
print(x)
"""
pembagi masing masing arange paling rendah adalah 2
1/[1]  = 1
4/[1]  = 4
7/[1]  = 7
10/[1] = 10
"""
