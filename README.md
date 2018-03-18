# Text-Recognizing

## Requirements

- python3

##### python3 packages:
- wikipedia
- nltk
- pytest


## Install requirements
To install requirements run:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ ./install_requirements.sh 
```


## Run languages base generation
Using `python3` run `generate_base.py` from `src` directory:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing/src$ python3 generate_base.py
```

`generate_base.py` has some optional arguments:

Options | Description 
--- | ---
-h, --help | Show this help message and exit
-l LANGUAGE, --language LANGUAGE | Article language (type abbreviation, for example 'en', 'pl'). Default: 'en'
-i ITERATIONS, --iterations ITERATIONS | Script iterations. Default: 100
-b BASE_FILE, --base_file BASE_FILE | Path to csv file where save data. Default="base.csv"
-c CORPUS_FILE, --corpus_file CORPUS_FILE | Path to txt file where save article texts. Default="corpus.txt"
-s SHORTEST_ARTICLE, --shortest_article SHORTEST_ARTICLE | Shortest article length (characters). Default=500


## Run tests
From `Text-Recognizing` directory run `run_test.sh`:
```commandline
bgorski@bgorski:~/workspace/Text-Recognizing$ ./run_tests.sh 
```
