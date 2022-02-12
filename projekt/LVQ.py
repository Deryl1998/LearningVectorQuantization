
from math import sqrt
from random import randrange
from random import seed
import time
import datetime

class LVQ(object):
  
    codeBook = None
    data = None
    learningRate = 0

    def __init__(self,data,n_codeBooks,codeBook=None):
       self.data = data
       self.codeBook = codeBook
       if self.codeBook is None: self.codeBook = [self.__RandomCodeBook(data) for i in range(n_codeBooks)]

    def __RandomCodeBook(self,data):
        length = len(data)
        columns = len(data[0])
        codeBook = [data[randrange(length)][i] for i in range(columns)]
        return codeBook

    def __EuclideanDistance(self,row1, row2):
        distance = 0.0
        for i in range(len(row1)-1):
            distance += (row1[i] - row2[i])**2
        return sqrt(distance)

    def __FindBestCodeBook(self,data, findRow):
        distance = list()
        for row in data:
            currentDistance = self.__EuclideanDistance(row, findRow)
            distance.append((row, currentDistance))
            distance.sort(key=lambda tup: tup[1])
        return distance[0][0]


    def Train(self,learningRate,epochs):
        seed(1)
        t0 = time.time()
        for epoch in range(epochs):
            learning = learningRate *(1.0 - (epoch/float(epochs)))
            errorSum = 0.0
            for row in self.data:
                bestCodeBook = self.__FindBestCodeBook(self.codeBook,row)
                for i in range(len(row)-1):
                    error = row[i] - bestCodeBook[i]
                    errorSum += error **2
                    if(bestCodeBook[-1] == row[-1]):
                        bestCodeBook[i] += learning * error
                    else:
                        bestCodeBook[i] -= learning * error
            print('>epoch=%d, learning=%.3f, errorSum=%.3f' % (epoch, learning, errorSum))
        print ("learning duration in seconds : %.2f" %(time.time() - t0))
        return self.codeBook

    def Predict(self, findRow):
        result = self.__FindBestCodeBook(self.codeBook, findRow)
        return result[-1]

    def Predictions(self,data):
        predicted = list()
        for row in data:
            out = self.Predict(row)
            predicted.append(out)
        return(predicted)

    def LearningDuration(self,data):
        predicted = self.Predictions(data)
        actualData = [row[-1] for row in data]
        correctness = 0
        for i in range(len(actualData)):
            print('correct answer = %.2f  predicted answer = %.2f' %(actualData[i],predicted[i]))
            if actualData[i] == predicted[i]:
                correctness += 1
        self.learningRate = correctness / float(len(actualData)) * 100.0
        print('Network accuracy: %.3f' % (self.learningRate))


               