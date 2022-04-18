import numpy as np

#行列を定義して，表示する
X1 = np.array([[1, 2, 3], [4, 5, 6]])
print("X1=\n{0}\n".format(X1))

X2 = np.array([[7, 8, 9], [0, 1, 2]])
print("X2=\n{0}\n".format(X2))

X3 = np.array([[2, 4], [6, 8], [0, 2]])
print("X3=\n{0}\n".format(X3))

X4 = np.array([[1, 2], [3, 4]])
print("X4=\n{0}\n".format(X4))

###計算###
print("------------計算-------------\n")
#和
print("X1+X2 =")
print(X1+X2)

#差
print("\n")
print("X1-X2 = ")
print(X1-X2)


#積
print("\n")
print("X1*X3 = ")
print(np.dot(X1,X3))

#逆行列
print("\n")
print("X4^-1 = ")
X4inv = np.linalg.inv(X4)
print(X4inv)




#補足
"""計算できない積はエラーを返す 2*3 と 2*3
ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
"""

#参考文献
#https://qiita.com/Nezura/items/4a6c56f1ee009ccb0c44
#https://www.teamxeppet.com/numpy-dot/
#https://deepage.net/features/numpy-inv.html