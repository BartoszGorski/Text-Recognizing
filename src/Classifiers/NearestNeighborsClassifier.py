import sys
sys.path.append('../')

from Interfaces.ClassificationModule import ClassificationModule
from Interfaces.ClassificationModule import LanguageType
from sklearn import neighbors
from sklearn import metrics
import numpy
#from sklearn import naive_bayes
#from sklearn import svm
#from sklearn import tree
#from sklearn import neural_network


class NearestNeighborsClassifier(ClassificationModule):
    def __init__(self, dataset = [[]], splitPoint = 0.5, neighborsNumber = 5):
        testDataset = self.splitDataset(dataset, splitPoint)
        self.classifier = neighbors.KNeighborsClassifier(neighborsNumber)

        self.classifier.fit(numpy.array(self.trainingDataset)[:,:-1], numpy.array(self.trainingDataset)[:,-1])

        testPrediction = self.classifier.predict(numpy.array(testDataset)[:,:-1])
        self.precision = round(metrics.accuracy_score(testPrediction, numpy.array(testDataset)[:,-1]) * 100, 2)
        print("Classifier precision is: ", self.precision)

    def predict(self, features = []):
        return LanguageType(self.classifier.predict(numpy.array(features).reshape(1, -1)))


#Fake data for classifier testing purpose. 
testData = [[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3],
[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3],
[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3],
[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3],
[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3],
[1,2,3,4,5.6,0], [13,5,5,5,2.3,1], [6,5,4,3,2.1,2], [10,9,8,7,6.5,3]]

testPredictionData = [1,2,3,4,5.6]

testKNN = NearestNeighborsClassifier(testData, 0.5)
print(testKNN.predict(testPredictionData))