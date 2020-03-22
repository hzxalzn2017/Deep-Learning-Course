sx = 0
sy = 0
m1 = 0
m2 = 0
x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
for i in range(len(x)):
    sx += x[i]  
    ValueX = sx / len(x)

for j in range(len(y)):
    sy / len(y)    
    ValueYS = sy / len(y)

for i in range(10):
    m1 += (x[i] - ValueX) * (y[i] - ValueYS)
    m2 += (x[i] - ValueX) * (x[i] - ValueX)   
w = m1/ m2
print("W的值为:",w)
b = ValueYS - w * ValueX
print("b的值为:",b)