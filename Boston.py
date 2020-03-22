import tensorflow as tf
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def Datainput():
    while(True):
        try :
            number = int (input("请选择属性:\n"))
            if 0<number & number<=13:
                break
            else:
                print("输入1-13之间的整数！！")
                continue
        except: 
            print("输入的数字有误！！")
            continue
    return number


def displayTitle(title):
    for i in range(len(title)):
        print("{}---{}".format(i+1,title[i]))

boston_housing = tf.keras.datasets.boston_housing
(x1, y1), (x2, y2) = boston_housing.load_data(test_split=0)

title = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B-1000", "LSTAT"]

displayTitle(title)
number = Datainput()
plt.figure()
plt.scatter(x1[:, number-1], y1)
plt.xlabel(title[number-1])
plt.ylabel("Price($1000/s)")
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.title(title[number-1] + " -- 散点图", x=0.5, y=1.02, fontsize=14)
plt.show()