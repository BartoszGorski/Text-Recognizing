from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

from src.Interfaces.ClassificationModule import ClassificationModule
from src.utils.FeaturesGen import prepare_corpus_dataset


class MultiLayerPerceptronClassifier(ClassificationModule):
    def __init__(self, dataset, splitPoint=0.2):
        X_train, X_test, y_train, y_test = self.splitDataset(dataset, splitPoint)

        self.mlp = MLPClassifier(hidden_layer_sizes=(40, 30, 20), max_iter=1000)
        self.mlp.fit(X_train, y_train)

        predictions = self.predict(X_test)

        print(confusion_matrix(y_test, predictions))
        print(classification_report(y_test, predictions))

    def predict(self, test_data):
        return self.mlp.predict(test_data)


dataset = prepare_corpus_dataset()
MultiLayerPerceptronClassifier(dataset)
