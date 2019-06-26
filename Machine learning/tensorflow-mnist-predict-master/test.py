import tensorflow.examples.tutorials.mnist.input_data as input_data  # 导入下载数据集手写体
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)  # 下载数据集

# print(type(mnist.train.images))  # 打印出数据类型 numpy.ndarray
# print(mnist.train.images.shape)  # 打印出数据结构 (55000, 784)
# print(mnist.train.labels.shape)  # 打印出one_hot (55000, 10)

from PIL import Image
import numpy as np

# np.array将数据转化为数组 np.reshape将一维数组reshape成(28*28)  mnist.train.images[1]取出第二张图片 dtype转换为int8数据类型
im_data = np.array(np.reshape(mnist.train.images[1], (28, 28)) * 255, dtype=np.int8)  # 取第一张图片的 数组
print(im_data)
# 将数组还原成图片 Image.fromarray方法 传入数组 和 通道
img = Image.fromarray(im_data, 'L')
img.save('test.jpg')
img.show()  # 显示图片

# 拿对应的标签
arr_data = mnist.train.labels[1]
print(arr_data)  # one-hot形式
