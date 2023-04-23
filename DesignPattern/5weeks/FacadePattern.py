# #========================절차지향적 프로그램

# import tensorflow as tf
# import matplotlib.pyplot as plt

# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_X, train_Y), (test_X, test_Y) = fashion_mnist.load_data()

# print(len(train_X), len(test_X))


# plt.imshow(train_X[0], cmap='gray')
# plt.colorbar()
# plt.show()

# print(train_Y[0])

# train_X = train_X / 255.0
# test_X = test_X /255.0

# train_X = train_X.reshape(-1, 28, 28, 1)
# test_X = test_X.reshape(-1, 28, 28, 1)


# print(train_X.shape, test_X.shape)

# model = tf.keras.Sequential([
#       tf.keras.layers.Conv2D(input_shape=(28,28,1), kernel_size=(3, 3), filters = 16),
#       tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=32),
#       tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=64),                               
#       tf.keras.layers.Flatten(),
#       tf.keras.layers.Dense(units=128, activation='relu'),
#       tf.keras.layers.Dense(units=10, activation='softmax')                        
# ])

# model.compile(optimizer=tf.keras.optimizers.Adam(),
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy']
#               )

# model.summary()

# history = model.fit(train_X, train_Y, epochs=25, validation_split=0.25)






#========================객체지향적 Facade 응용


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

class DataProcess:

  def __init__(self):
    self.train_X = 0
    self.train_Y = 0
    self.test_X = 0
    self.test_Y = 0

    self.N = 0
    self.dimX = 0
    self.dimY = 0

  def setImageDim(self):
    self.N = len(self.train_X)

    imageCase = self.train_X[0]
    self.dimY = imageCase.shape[0]
    self.dimX = imageCase.shape[1]

  def readDataset(self):
    fashion_mnist = tf.keras.datasets.fashion_mnist
    (self.train_X, self.train_Y), (self.test_X, self.test_Y) = fashion_mnist.load_data()
    self.setImageDim()

  def normalize(self):
    # 0~1 normalize
    self.train_X = self.train_X / 255.0
    self.test_X = self.test_X /255.0

  def trainReady(self):
    #reshape the image dimension to (#, 28, 28, 1)
    self.train_X = self.train_X.reshape(-1, self.dimY, self.dimX, 1)
    self.test_X = self.test_X.reshape(-1, self.dimY, self.dimX, 1)

  def showStatus(self):
    print("DP: 총", self.N, "장의 이미지가 로드되었습니다.")
    print("DP: 각 이미지 크기는 ", self.dimY, "X", self.dimX, "입니다.")
    

  
class DeepLearning:
  
  def __init__(self):
    self.model = tf.keras.Sequential()
    self.optimizer = tf.keras.optimizers.Adam()
    self.data_X = 0
    self.data_Y = 0

    self.epoch = 0
    self.validation_split = 0
    
  def setEpoch(self, epoch):
    self.epoch = epoch
    return self
  
  def setValidSplitRatio(self, split_ratio):
    self.validation_split = split_ratio
    return self

  def setInputData(self, X, Y):
    self.data_X = X
    self.data_Y = Y
    return self

  def setLayers(self):
    self.model.add(tf.keras.layers.Conv2D(input_shape=(28,28,1), kernel_size=(3, 3), filters = 16))
    self.model.add(tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=32))
    self.model.add(tf.keras.layers.Conv2D(kernel_size=(3, 3), filters=64))
    self.model.add(tf.keras.layers.Flatten())
    self.model.add(tf.keras.layers.Dense(units=128, activation='relu'))
    self.model.add(tf.keras.layers.Dense(units=10, activation='softmax'))

  def compileDL(self):
    self.model.compile(optimizer=self.optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
              )
    
  def showModelSummary(self):
    self.model.summary()

  def goTrain(self):
    print("DL: 학습을 시작합니다.")
    history = self.model.fit(self.data_X, self.data_Y, epochs=self.epoch, validation_split=self.validation_split)


class Visualize:
  def __init__(self):
    pass

  def showImage(self, image):
    print("VS: 이미지를 출력합니다.")
    plt.imshow(image, cmap='gray')
    plt.colorbar()
    plt.show()


#FACADE
class Learning:

  def __init__(self):
    self.DP = DataProcess()
    self.VS = Visualize()
    self.DL = DeepLearning()
  
  def learn(self):
    self.DP.readDataset()
    self.VS.showImage(self.DP.train_X[0])
    self.DP.normalize()
    self.DP.trainReady()
    self.DP.showStatus()
    self.DL.setInputData(self.DP.train_X, self.DP.train_Y).setEpoch(25).setValidSplitRatio(0.2)
    self.DL.setLayers()
    self.DL.compileDL()
    self.DL.goTrain()



#======================main
learn = Learning()
learn.learn()