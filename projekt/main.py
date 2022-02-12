from LVQ import LVQ
import pandas as pd
import numpy as np
import os



def loadData(filePath):
    data= pd.read_csv(filePath,sep=';',dtype='str',header=None)
    data = data.apply(np.float64)
    data = data.values
    return data

def saveCodeBook(wektor):
    filePatch = os.path.realpath('..') + '\\data\\codeBook.csv'
    df = pd.DataFrame(data=wektor)
    df.to_csv(filePatch,sep=';',float_format='%g',header=None, index=None)

trainDataPath = os.path.realpath('..') + '\\data\\data.csv'
codeBookPath = os.path.realpath('..') + '\\data\\codeBook.csv'

#codeBook = loadData(codeBookPath)
lvq = LVQ (loadData(trainDataPath),500,None)

lvq.Train(0.75,10)
lvq.LearningDuration(lvq.data)
saveCodeBook(lvq.codeBook)

#testingData = [1.51751,12.81,3.57,1.35,73.02,0.62,8.59,1.00,0.10]
#print(lvq.Predict(testingData))
#print('CodeBook')
#print(lvq.codeBook)



