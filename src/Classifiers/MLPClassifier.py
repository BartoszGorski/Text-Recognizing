from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

from src.Interfaces.ClassificationModule import ClassificationModule
from src.utils.FeaturesGen import prepare_corpus_dataset


class MultiLayerPerceptronClassifier(ClassificationModule):
    def __init__(self, dataset, splitPoint=0.2):
        X_train, X_test, y_train, y_test = self.splitDataset(dataset, splitPoint)

        self.classifier = MLPClassifier(hidden_layer_sizes=(40, 30, 20), max_iter=1000)
        self.classifier.fit(X_train, y_train)

        prediction = self.predict(X_test)

        print(confusion_matrix(y_test, prediction))
        print(classification_report(y_test, prediction))


dataset = prepare_corpus_dataset()
MultiLayerPerceptronClassifier(dataset)
