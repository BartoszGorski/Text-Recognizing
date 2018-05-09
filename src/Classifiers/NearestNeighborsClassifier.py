from sklearn import neighbors
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import numpy

from src.Interfaces.ClassificationModule import ClassificationModule
from src.utils.FeaturesGen import prepare_corpus_dataset


class NearestNeighborsClassifier(ClassificationModule):
    def __init__(self, dataset, splitPoint=0.2, neighborsNumber = 5):
        X_train, X_test, y_train, y_test = self.splitDataset(dataset, splitPoint)
        self.classifier = neighbors.KNeighborsClassifier(neighborsNumber)
        self.classifier.fit(X_train, y_train)

        prediction = self.predict(X_test)

        print(confusion_matrix(y_test, prediction))
        print(classification_report(y_test, prediction))

    def predict(self, features):
        return self.classifier.predict(features)


dataset = prepare_corpus_dataset()
NearestNeighborsClassifier(dataset)
