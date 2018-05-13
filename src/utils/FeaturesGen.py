import re
import string
import csv
import nltk
nltk.download('punkt')

from src.Interfaces.ClassificationModule import LanguageType


VOWELS = 'aeiouyAEIOUY'
LETTERS = string.ascii_lowercase

'''
Legend:
index - name

analysed text array:
0 - language type,
1 - average_word_length,
2 - vowels_ratio,
3 - average_words_count,
4 - non_ascii_ratio,
5 - spaces_ratio,
doubles_ratio:
6 - doubles_characters,
7 - doubles_asci_letters,
8 - doubles_vowels,
letter_ratio (lower and upper case):
9 - A,
10 - B,
11 - C,
...
32 - X,
33 - Y,
34 - Z,
'''


class FeaturesGen:
    def __init__(self, csv_newline='', csv_delimiter=',', csv_quoting=csv.QUOTE_ALL):
        self.newline = csv_newline
        self.delimiter = csv_delimiter
        self.quoting = csv_quoting

    def generate_features(self, corpus_file, language):
        sentences = self.__extract_sentences(corpus_file)
        sentences_length = len(sentences)
        analysed_text = []
        for idx, sentence in enumerate(sentences):
            analysed_sentence = self.analyse_text(sentence, language)
            if analysed_sentence is None:
                continue
            analysed_text.append(analysed_sentence)
            print("Analysed {} out of {} sentences.".format(idx + 1, sentences_length))
        return analysed_text

    def __extract_sentences(self, corpus_file):
        sentences = []
        with open(corpus_file, newline=self.newline) as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter, quoting=self.quoting)
            for row in reader:
                sentences.append(row[0])
        return sentences

    def analyse_text(self, text, language):
        words = self.extract_tokens(text)
        if len(words) <= 0:
            return
        average_word_length = self.average_word_length(words)
        vowel_ratio = self.vowel_ratio(text)
        non_ascii_ratio = self.non_ascii_ratio(text)
        doubles_ratio = self.double_letter_and_vowels_ratio(text)
        letter_ratio = self.alphabet_ratio(text)
        spaces_ratio = self.spaces_ratio(text)
        analysed_text = [language, average_word_length, vowel_ratio, len(words),
                         non_ascii_ratio, spaces_ratio]
        analysed_text.extend(doubles_ratio)
        analysed_text.extend(letter_ratio)
        return analysed_text

    def extract_tokens(self, text):
        return nltk.wordpunct_tokenize(text)

    def average_word_length(self, words):
        words_len = len(words)
        return sum(len(word) for word in words) / words_len if words_len else 0

    def vowel_ratio(self, text):
        vowels_count = len(re.findall('[{}]'.format(VOWELS), text))
        vowel_ratio = self.__ratio_in_text(text, vowels_count)
        return vowel_ratio

    def spaces_ratio(self, text):
        spaces_count = len(re.findall(' ', text))
        spaces_ratio = self.__ratio_in_text(text, spaces_count)
        return spaces_ratio

    def __ratio_in_text(self, text, variable_count):
        text_len = len(text)
        return variable_count / text_len

    def non_ascii_ratio(self, text):
        non_ascii = len(re.sub('[\x20-\x7e]', '', text))
        return non_ascii / len(text)

    def double_letter_and_vowels_ratio(self, text):
        doubles_characters = 0
        doubles_asci_letter = 0
        doubles_vowel = 0

        text = text.lower()
        character_iterator = iter(text)
        last_character = next(character_iterator)
        is_last_vowel = last_character in VOWELS
        for character in character_iterator:
            is_letter = character in LETTERS
            is_vowel = character in VOWELS

            if character == last_character and is_letter:
                doubles_asci_letter += 1

            if character == last_character:
                doubles_characters += 1

            if is_last_vowel and is_vowel:
                doubles_vowel += 1
            is_last_vowel = is_vowel

            last_character = character
        return [
            self.__ratio_in_text(text, doubles_characters),
            self.__ratio_in_text(text, doubles_asci_letter),
            self.__ratio_in_text(text, doubles_vowel),
        ]

    def alphabet_ratio(self, text):
        letter_ratio = []
        for letter in LETTERS:
            letter_count = 0
            lower_case_text = text.lower()
            letter_count += lower_case_text.count(letter)
            letter_ratio.append(self.__ratio_in_text(text, letter_count))
        return letter_ratio


def prepare_corpus_dataset():
    fg = FeaturesGen()
    pl_corpus = fg.generate_features("../../corpus/plCorpus.csv", LanguageType.polish.value)
    en_corpus = fg.generate_features("../../corpus/engCorpus.csv", LanguageType.english.value)
    nl_corpus = fg.generate_features("../../corpus/nonLanguageCorpus.csv", LanguageType.unnatural.value)
    cd_corpus = fg.generate_features("../../corpus/codeCorpus.csv", LanguageType.code.value)
    rn_corpus = fg.generate_features("../../corpus/rnCorpus.csv", LanguageType.random.value)
    min_lenght = min(len(pl_corpus), len(en_corpus), len(nl_corpus), len(cd_corpus), len(rn_corpus))
    print("Taking {} samples from each corpus".format(min_lenght))
    print("pl_corpus {}".format(len(pl_corpus)))
    print("en_corpus {}".format(len(en_corpus)))
    print("nl_corpus {}".format(len(nl_corpus)))
    print("cd_corpus {}".format(len(cd_corpus)))
    print("rn_corpus {}".format(len(rn_corpus)))
    corpus = []
    corpus.extend(pl_corpus[:min_lenght])
    corpus.extend(en_corpus[:min_lenght])
    corpus.extend(nl_corpus[:min_lenght])
    corpus.extend(cd_corpus[:min_lenght])
    corpus.extend(rn_corpus[:min_lenght])
    return corpus
