from enum import Enum
from sklearn import naive_bayes
from sklearn.metrics import classification_report, confusion_matrix

from src.Interfaces.ClassificationModule import ClassificationModule
from src.utils.FeaturesGen import prepare_corpus_dataset


class NBType(Enum):
    gauss = 0
    bernoulli = 1
    multinomial = 2


class NaiveBayesClassifier(ClassificationModule):
    def __init__(self, dataset, splitPoint=0.2, type = NBType.gauss.value):
        X_train, X_test, y_train, y_test = self.splitDataset(dataset, splitPoint)
        
        if type == NBType.gauss.value:
            self.classifier = naive_bayes.GaussianNB()
        elif type == NBType.bernoulli.value:
            self.classifier = naive_bayes.BernoulliNB()
        else:
            self.classifier = naive_bayes.MultinomialNB()

        self.classifier.fit(X_train, y_train)

        prediction = self.predict(X_test)

        print(confusion_matrix(y_test, prediction))
        print(classification_report(y_test, prediction))


dataset = prepare_corpus_dataset()
NaiveBayesClassifier(dataset, NBType.bernoulli.value)
