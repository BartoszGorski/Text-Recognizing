# Text-Recognizing

## Requirements

- python3

##### python3 packages:
- sklearn
- nltk
- pytest


## Install requirements
To install requirements run:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ ./install_requirements.sh 
```


## Classify text

Classify text and save result to json file.

usage: python3 classify_text.py [-h] [-c CLASSIFIER] text_file output_file

positional arguments: 

Argument | Description 
--- | --- 
text_file | Path to text file to analyze  
output_file | Json output file with classification result  

optional arguments:  

Options | Description 
--- | ---
-h, --help | Show help message and exit
-c CLASSIFIER, --classifier CLASSIFIER | Choose classifier: -"MLP" = Multi Layer Perceptron Classifier, -"NNC" = Nearest Neighbors Classifier, -"SVM" = Support Vector Machine Classifier. Default one is MLP

             
Example of usage
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ python3 classify_text.py /home/bgorski/my_text.txt result/result_file.json
```

```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ python3 classify_text.py my_text.txt result_file.json -c SVM
```

## GUI text classifier
Using `python3` run `gui_text_analiser.py` from `Text-Recognizing` directory:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing/src$ python3 gui_text_analiser.py
```

## Generate pkl files
Using `python3` run `train_classifiers.py` from `Text-Recognizing` directory:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing/src$ python3 train_classifiers.py
```

Corpses are needed to train classifiers. They have to be in `Text-Recognizing/corpus/*` 

## Run tests
From `Text-Recognizing` directory run `run_test.sh`:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ ./run_tests.sh 
```
