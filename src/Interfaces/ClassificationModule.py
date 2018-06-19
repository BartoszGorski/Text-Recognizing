from enum import Enum
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


class LanguageType(Enum):
    garbage = 0
    polish = 1
    english = 2
    code = 3
    random = 4


class ClassifierFitting(Enum):
    ok = 0
    under = 1
    over = 2


class ClassificationModule:
    #This method initializes whole module. It shall train/create classifier and calculate precision.
    #It shall also split the dataset in 'splitPoint' and save it to 'trainingDataset'.
    def __init__(self, dataset, splitPoint=0.2):
        raise NotImplementedError

    #This method is used to classify sample to one of available LanguageTypes depending on its features values.
    #Returned value is enum LanguageType
    def predict(self, test_data):
        return self.classifier.predict(test_data)

    #Common method for splitting dataset thath should be used in constructor. Returns testDataset.
    def splitDataset(self, dataset, splitPoint=0.2):
        X = []
        y = []
        for i in range(len(dataset)):
            X.append(dataset[i][1:])
            y.append(dataset[i][0])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=splitPoint)
        return X_train, X_test, y_train, y_test

    #Method for detecting under/overfitting of classifier. Returns ClassifierFitting enum value.
    def checkFitting(self, X_train, X_test, y_train, y_test, tolerance = 0.1):
        trainingDatasetPrediction = self.predict(X_train)
        testDatasetPrediction = self.predict(X_test)

        trainingDatasetAccuracy = accuracy_score(y_train, trainingDatasetPrediction) * 100
        testDatasetAccuracy = accuracy_score(y_test, testDatasetPrediction) * 100

        print("checkFitting:: Training dataset accuracy: ", trainingDatasetAccuracy)
        print("checkFitting:: Test dataset accuracy: ", testDatasetAccuracy)

        maxTolerance = (1.0 + tolerance) * trainingDatasetAccuracy
        minTolerance = (1.0 - tolerance) * trainingDatasetAccuracy

        if testDatasetAccuracy > maxTolerance:
            fittingResult = ClassifierFitting.under
            print("checkFitting:: Classifier UNDERFITTING detected!!!")
        elif testDatasetAccuracy < minTolerance:
            fittingResult = ClassifierFitting.over
            print("checkFitting:: Classifier OVERFITTING detected!!!")
        else:
            fittingResult = ClassifierFitting.ok
            print("checkFitting:: Classifier fitted OK!!!")

        return fittingResult

    @staticmethod
    def save_classifier(classifier, filename):
        joblib.dump(classifier, filename)

    @staticmethod
    def load_classifier(filename):
        return joblib.load(filename)

    #This float represents how accurate the module is. Precision is calculated in the following way:
    # 1. Whole dataset is splitted into: trainingDataset and testDataset.
    # 2. Module is being learnt/created with use of trainingDataset.
    # 3. Module predicts classes(LanguageType) for samples from testDataset(which we already know :]).
    # 4. Module's predicitons on testDataset are being compared to real ones.
    # 5. Precision = (moduleSuccessfulPredicitonsOnTestDataset / allPredictionsOnTestDataset) * 100%
    # Precision should be calculated during construction of this object. 
    precision = float()

    #Dataset fragment which is used to train/create classification module.
    trainingDataset = []
