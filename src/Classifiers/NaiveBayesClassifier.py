import sys
from enum import Enum
sys.path.append('../')

from Interfaces.ClassificationModule import ClassificationModule
from Interfaces.ClassificationModule import LanguageType
from sklearn import naive_bayes
from sklearn import metrics
import numpy


class NBType(Enum):
    gauss = 0
    bernoulli = 1
    multinomial = 2


class NaiveBayesClassifier(ClassificationModule):
    def __init__(self, dataset = [[]], type = NBType.gauss, splitPoint = 0.5):
        testDataset = self.splitDataset(dataset, splitPoint)
        
        if type == NBType.gauss:
            self.classifier = naive_bayes.GaussianNB()
        elif type == NBType.bernoulli:
            self.classifier = naive_bayes.BernoulliNB()
        else:
            self.classifier = naive_bayes.MultinomialNB()

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

testPredictionData = [1,1,1,1,1.6]

#testNB = NaiveBayesClassifier(testData, NBType.bernoulli, 0.5)
#print(testNB.predict(testPredictionData))