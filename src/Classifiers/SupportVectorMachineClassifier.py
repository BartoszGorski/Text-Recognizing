from enum import Enum
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

from src.Interfaces.ClassificationModule import ClassificationModule
from src.utils.FeaturesGen import prepare_corpus_dataset


class SVMType(Enum):
    linear = 0
    nu = 1
    c = 2


class SupportVectorMachineClassifier(ClassificationModule):
    def __init__(self, dataset, splitPoint=0.2, type=SVMType.linear.value):
        X_train, X_test, y_train, y_test = self.splitDataset(dataset, splitPoint)
        
        if type == SVMType.linear.value:
            self.classifier = svm.LinearSVC()
        elif type == SVMType.nu.value:
            self.classifier = svm.NuSVC()
        else:
            self.classifier = svm.SVC()

        self.classifier.fit(X_train, y_train)
        self.checkFitting(X_train, X_test, y_train, y_test)

        prediction = self.predict(X_test)

        print(confusion_matrix(y_test, prediction))
        print(classification_report(y_test, prediction))


dataset = prepare_corpus_dataset()
SupportVectorMachineClassifier(dataset, type=SVMType.linear.value)
