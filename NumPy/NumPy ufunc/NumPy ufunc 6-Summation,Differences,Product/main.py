# summation, differences, product

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print("summation".center(20, "-"))
print(f"array a = {a}")
print(f"array b = {b}")
print(f"sum array a = {np.sum(a)}")
print(f"sum array b = {np.sum(b)}")
print(
    f"sum masing-masing array, lalu hasil dimasukkan dalam array hasil = {np.sum([a, b],axis=1)}"
)
print(f"add array a dan b, lalu sum array = {np.sum([a, b])}")
print(f"cumulative sum a = {np.cumsum(a)}")
print(f"cumulative sum b = {np.cumsum(b)}")
print(f"cumulative sum a dan b = \n{np.cumsum([a,b],axis=1)}")
print(f"cumulative sum a dan b = {np.cumsum([a,b])}")
"""
array a dan b di lakukan stacking menjadi satu array, lalu dilakukan cumulative sum
"""

print("\n")
print("differences".center(20, "-"))
print(f"array a = {a}")
print(f"array b = {b}")
print(f"differences b = {np.diff(a)}")
print(f"differences a = {np.diff(b)}")
"""
diff = pengurangan array index ke ((n+1)-n)
"""
print(f"differences a dan b = \n{np.diff([a,b])}")
print(f"differences a = {np.diff(a,n=1)}")
print(f"differences a = {np.diff(a,n=2)}")
print(f"differences a = {np.diff(a,n=3)}")
print(f"differences a = {np.diff(a,n=4)}")
"""
parameter n adalah berapa kali difference dilakukan
"""

print("\n")
print("product".center(20, "-"))
print(f"array a = {a}")
print(f"array b = {b}")
print(f"prod array a = {np.prod(a)}")
print(f"prod array b = {np.prod(b)}")
print(
    f"prod masing-masing array, lalu hasil dimasukkan dalam array hasil = {np.prod([a, b],axis=1)}"
)
print(f"add array a dan b, lalu prod array = {np.prod([a, b])}")
print(f"cumulative prod a = {np.cumprod(a)}")
print(f"cumulative prod b = {np.cumprod(b)}")
print(f"cumulative prod a dan b = \n{np.cumprod([a,b],axis=1)}")
print(f"cumulative prod a dan b = {np.cumprod([a,b])}")
"""
array a dan b di lakukan stacking menjadi satu array, lalu dilakukan cumulative sum
"""
