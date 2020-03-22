import numpy as np

x1 = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
x2 = [2, 3, 4, 2, 3, 4, 2, 4, 1, 3]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
x0 = np.ones(10)

X = np.stack((x0, x1, x2), axis=1)
X = np.mat(X)

Y = np.array(y).reshape(-1, 1)
Y = np.mat(Y)

w = (X.T * X).I * X.T * Y
print("W的shape属性结果为：",np.shape(w))
print("X=", X, "\nY=", Y, "\nw=", w)