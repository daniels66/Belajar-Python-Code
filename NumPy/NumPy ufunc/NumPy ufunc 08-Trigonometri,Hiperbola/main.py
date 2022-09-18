# trigonometri dan hiperbola dalam numpy

import numpy as np

a = np.pi / 2
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])

print("Trigonometri".center(30, "-"))
"""
sin()
cos()
tan()
"""

print("array =", arr)
x = np.sin(a)
print("sin =", x)
x = np.cos(a)
print("cos =", x)
x = np.tan(a)
print("tan =", x)
"""
setiap index dalam array dilakukan sin,cos,tan
"""
x = np.sin(arr)
print("sin =\n", x)
x = np.cos(arr)
print("cos =\n", x)
x = np.tan(arr)
print("tan =\n", x)
"""
Secara default semua fungsi trigonometri mengambil radian sebagai parameter 
tetapi dapat mengonversi radian ke derajat dan sebaliknya juga di NumPy.
dengan menggunakan np.deg2rad()
"""
deg = np.array([90, 180, 270, 360])
x = np.deg2rad(deg)
print("degree ke radian =\n", x)

print("Hiperbola".center(30, "-"))
"""
sinh()
cosh()
tanh()
arcsinh()
arccosh()
arctanh()
"""

print("array =", arr)
x = np.sinh(a)
print("sinh =", x)
x = np.cosh(a)
print("cosh =", x)
x = np.tanh(a)
print("tanh =", x)
"""
setiap index dalam array dilakukan sinh,cosh,tanh
"""
x = np.sinh(arr)
print("sinh =\n", x)
x = np.cosh(arr)
print("cosh =\n", x)
x = np.tanh(arr)
print("tanh =\n", x)

"""
Menemukan sudut dari nilai sinus hiperbolik, cos, tan. 
Misalnya. sinh, cosh dan tanh 
kebalikan (arcsinh, arccosh, arctanh).

Numpy menyediakan ufuncs arcsinh(), arccosh() dan arctanh() 
yang menghasilkan nilai radian untuk nilai sinh, cosh, dan tanh yang diberikan.
"""
x = np.arcsinh(a)
print("arcsinh =", x)
x = np.arccosh(a)
print("arccosh =", x)
