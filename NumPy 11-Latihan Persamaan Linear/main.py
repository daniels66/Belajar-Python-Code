# menyelesaikan persamaan linear
# untuk pembelajaran materi inil ebih lanjut silahkan pelajari aljabar linear

import numpy as np

"""
y = a * x
y1 = 2 x1 + 3 x2
y2 = x1 + 2 x2

jika x1 = 4, dan x2 = 5
y1 = 2 * 4 + 3 * 5 = 23
y2 = 4 + 2 * 5 = 14

y1 dan y2 apabila dijadikan matrix 
[[2 3]  dot [[x1]  = [[23]
 [1 2]]      [x2]]    [14]]

apabila ingin mencari nilai x1 dan x2 dapat dilakukan
y = a * x
x = a inverse * y
"""
print("persamaan linear".center(20, "-"))
a1 = np.array([[2, 3], [1, 2]])
y = np.array([23, 14])
x = np.array(["x1", "x2"])
print(a1, "\ndot\n", x.reshape(2, 1), "\n=\n", y.reshape(2, 1))

# untuk mencari nilai x1 dan x2
a1_inv = np.linalg.inv(a1)
hasil_x = np.dot(a1_inv, y)
print("nilai x adalah =\n", hasil_x)
print("nilai dari x1 adalah = ", hasil_x[0])
print("nilai dari x2 adalah = ", hasil_x[1])

# selain menggunakan cara diatas dapat menggunakan
# np.linalg.solve(a1,y) fungsi tersebut tidak memerlukan inverse a1
hasil_x2 = np.linalg.solve(a1, y)
print("nilai x menggunakan np.linalg.solve() =\n", hasil_x2)
