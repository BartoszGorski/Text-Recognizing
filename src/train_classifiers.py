from utils.FeaturesGen import prepare_corpus_dataset

from Classifiers.MLPClassifier import MultiLayerPerceptronClassifier
from Classifiers.NaiveBayesClassifier import NaiveBayesClassifier, NBType
from Classifiers.NearestNeighborsClassifier import NearestNeighborsClassifier
from Classifiers.SupportVectorMachineClassifier import SupportVectorMachineClassifier
from Classifiers.SupportVectorMachineClassifier import SVMType


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
