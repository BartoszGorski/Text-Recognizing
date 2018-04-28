from enum import Enum

class LanguageType(Enum):
    unnatural = 0
    polish = 1
    english = 2

class ClassificationModule:
    #This method initializes whole module. It shall train/create classifier and calculate precision.
    #It shall also split the dataset in 'splitPoint' and save it to 'trainingDataset'.
    def __init__(self, dataset = [], splitPoint = 0.5):
        raise NotImplementedError

    #This method is used to classify sample to one of available LanguageTypes depending on its features values.
    #Returned value is enum LanguageType
    def predict(self, features = []):
        raise NotImplementedError

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
