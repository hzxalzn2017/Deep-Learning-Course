import tensorflow as tf

x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
x1 = tf.reduce_mean(x)
y1 = tf.reduce_mean(y)

up = tf.reduce_sum(tf.multiply(x-x1, y-y1))
down = tf.reduce_sum(tf.pow(x-x1, 2))
w = up/down
b = y1 - w * x1
print("w={}".format(w))
print("b={}".format(b))

