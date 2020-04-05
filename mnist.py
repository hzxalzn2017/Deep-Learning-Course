import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data("D:\mydatasets\mnist.npz") 
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.figure(figsize=(10,10))
plt.suptitle("MNIST测试集样本",fontsize=20,color="red")

for i in range(16):
    num = np.random.randint(1,50000)

    plt.subplot(4,4,i+1)
    plt.axis("off")
    plt.imshow(train_x[num],cmap='gray')
    plt.title("标签值:" + str(train_y[num]))

plt.show()