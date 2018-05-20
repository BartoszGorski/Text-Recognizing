from Interfaces.ClassificationModule import ClassificationModule, LanguageType
from utils.FeaturesGen import FeaturesGen

classifier = ClassificationModule.load_classifier('MLP.pkl')
fg = FeaturesGen()

while True:
    text = input('Enter your text: ')
    if text == '':
        continue
    analysed_test = fg.analyse_text(text)[1:]
    prediction = classifier.predict([analysed_test])
    print("Prediction language: {} {}".format(prediction, LanguageType(prediction).name))
