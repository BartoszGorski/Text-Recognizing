from src.utils.FeaturesGen import prepare_corpus_dataset

from src.Classifiers.MLPClassifier import MultiLayerPerceptronClassifier
from src.Classifiers.NaiveBayesClassifier import NaiveBayesClassifier, NBType
from src.Classifiers.NearestNeighborsClassifier import NearestNeighborsClassifier
from src.Classifiers.SupportVectorMachineClassifier import SupportVectorMachineClassifier
from src.Classifiers.SupportVectorMachineClassifier import SVMType


dataset = prepare_corpus_dataset()
print(
    ''' 
    
    *** MultiLayerPerceptron ***
    '''
)
MultiLayerPerceptronClassifier(dataset)

print(
    ''' 

    *** NaiveBayesClassifier ***
    '''
)
NaiveBayesClassifier(dataset, type=NBType.gauss.value)

print(
    ''' 

    *** NearestNeighborsClassifier ***
    '''
)
NearestNeighborsClassifier(dataset)

print(
    ''' 

    *** SupportVectorMachineClassifier ***
    '''
)
SupportVectorMachineClassifier(dataset, type=SVMType.linear.value)
