import tensorflow as tf
import numpy as np

x=tf.constant([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
y=tf.constant([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y0 =tf.constant([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00,45.00, 78.50, 69.65, 75.69, 95.30])
x0=np.ones(len(x))
X=np.stack((x0,x,y),axis=1)
Y=np.array(y0).reshape(-1,1)
t=np.transpose(X)
one=np.linalg.inv(np.matmul(t,X))
one_t=np.matmul(one,t)
W=np.matmul(one_t,Y)
W=W.reshape(-1)
def Input():
    while(True):
        try :
            a = float (input("输入商品房面积(20-500之间的实数)："))
            b = int (input("输入房间数(1-10之间的整数)： "))
            if a in range(20,500) and b in range(1,10):
               break
        except: 
            print("ERROR:Please input again。")
            continue
      
    return a, b

a, b = Input()
result=W[1]*a+W[2]*b+W[0]
print("预测房价：",round(result,2),"万元")