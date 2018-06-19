import os
import argparse
import json

from src.Interfaces.ClassificationModule import ClassificationModule, LanguageType
from src.utils.FeaturesGen import FeaturesGen


def save_json_result(json_path, language_type):
    with open(json_path, 'w') as outfile:
        json.dump({"result": language_type}, outfile)


def classify_result(prediction_result):
    result_name = LanguageType(prediction_result).name
    if result_name == "garbage" or result_name == "code" or result_name == "random":
        language_type = "non_natural"
    else:
        language_type = LanguageType(prediction_result).name
    return language_type


def choose_classifier(classifier_type):
    if classifier_type == "NNC":
        print("Using \"NNC\"")
        return ClassificationModule.load_classifier('classifiers_pkl/NearestNeighbors.pkl')
    elif classifier_type == "SVM":
        print("Using \"SVM\"")
        return ClassificationModule.load_classifier('classifiers_pkl/SVM.pkl')
    elif classifier_type == "MLP":
        print("Using \"MLP\"")
        return ClassificationModule.load_classifier('classifiers_pkl/MLP.pkl')
    else:
        print("Wrong classifier type."
              " Next time choose one of these: \"MLP\", \"NNC\", \"SVM\".")
        print("Using \"MLP\"")
        return ClassificationModule.load_classifier('classifiers_pkl/MLP.pkl')


def get_text(text_file):
    if not os.path.isfile(text_file):
        raise IOError('File {} does not exist.'.format(text_file))
    with open(text_file) as file:
        return file.read()


def runner(args):
    feature_generator = FeaturesGen()
    classifier = choose_classifier(args.classifier)
    analysed_test = feature_generator.analyse_text(get_text(args.text_file))[1:]
    prediction = classifier.predict([analysed_test])
    language_type = classify_result(prediction)
    save_json_result(args.output_file, language_type)
    print("Classify result: {} language".format(language_type))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze text.')
    parser.add_argument('text_file', type=str, help='Path to text file to analyze')
    parser.add_argument('output_file', type=str,
                        help='Json output file with classification result')
    parser.add_argument('-c', '--classifier', default="MLP",
                        help='Choose classifier: '
                             '-\"MLP\" = Multi Layer Perceptron Classifier, '
                             '-\"NNC\" = Nearest Neighbors Classifier, '
                             '-\"SVM\" = Support Vector Machine Classifier. '
                             'Default one is MLP')
    args = parser.parse_args()
    runner(args)
