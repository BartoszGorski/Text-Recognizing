import re
import string
import csv
import nltk
nltk.download('punkt')

VOWELS = 'aeiouyAEIOUY'
LETTERS = string.ascii_lowercase


class FeaturesGen:
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
        with open(corpus_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
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
        return {
            'language': language,
            'word_length': average_word_length,
            'vowel_ratio': vowel_ratio,
            'words_in_sentence': len(words),
            'non_ascii_ratio': non_ascii_ratio,
            'doubles_ratio': doubles_ratio,
            'letter_ratio': letter_ratio,
        }

    def extract_tokens(self, text):
        return nltk.wordpunct_tokenize(text)

    def average_word_length(self, words):
        words_len = len(words)
        return sum(len(word) for word in words) / words_len if words_len else 0

    def vowel_ratio(self, text):
        vowels_count = len(re.findall('[{}]'.format(VOWELS), text))
        vowel_ratio = self.__ratio_in_text(text, vowels_count)
        return vowel_ratio

    def __ratio_in_text(self, text, variable_count):
        text_len = len(text)
        return variable_count / text_len

    def non_ascii_ratio(self, text):
        non_ascii = len(re.sub('[\x20-\x7e]', '', text))
        return non_ascii / len(text)

    def double_letter_and_vowels_ratio(self, text):
        doubles_characters = 0
        doubles_letter = 0
        doubles_vowel = 0

        text = text.lower()
        character_iterator = iter(text)
        last_character = next(character_iterator)
        is_last_vowel = last_character in VOWELS
        for character in character_iterator:
            is_letter = character in LETTERS
            is_vowel = character in VOWELS

            if character == last_character and is_letter:
                doubles_letter += 1

            if character == last_character:
                doubles_characters += 1

            if is_last_vowel and is_vowel:
                doubles_vowel += 1
            is_last_vowel = is_vowel

            last_character = character
        doubles = {
            'doubles_characters' : self.__ratio_in_text(text, doubles_characters),
            'doubles_asci_letters': self.__ratio_in_text(text, doubles_letter),
            'doubles_vowels' : self.__ratio_in_text(text, doubles_vowel),
        }
        return doubles

    def alphabet_ratio(self, text):
        letter_ratio = []
        for letter in LETTERS:
            letter_count = 0
            lower_case_text = text.lower()
            letter_count += lower_case_text.count(letter)
            letter_ratio.append(self.__ratio_in_text(text, letter_count))
        return letter_ratio
