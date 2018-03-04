import re
import string
import nltk
nltk.download('punkt')

from base_gen.ArticleGetter import get_random_page


VOWELS = 'aeiouyAEIOUY'
LETTERS = string.ascii_lowercase


class BaseGen:

    def collect_articles_date(self, language='en', shortest_summary=500):
        page_not_found = True
        analysed = {}
        while page_not_found:
            page = get_random_page(language)
            summary = self.__chop_summary(page.summary)
            if len(summary) < shortest_summary:
                continue
            page_not_found = False
            analysed = self.__analyse_text(summary)
            analysed['language'] = language
            analysed['page_id']  = page.pageid
        return analysed

    def __chop_summary(self, summary):
        return summary.split("\n\n")[0]

    def __analyse_text(self, text):
        words = self.extract_words(text)
        average_word_length = self.average_word_length(words)
        vowel_ratio = self.vowel_ratio(words)
        average_words_in_sentences = self.average_words_in_sentences(len(words), text)
        non_ascii_ratio = self.non_ascii_ratio(text)
        doubles_ratio = self.double_letter_and_vowels_ratio(words)
        letter_ratio = self.alphabet_ratio(words)
        return {
            'word_length': average_word_length,
            'vowel_ratio': vowel_ratio,
            'words_in_sentences': average_words_in_sentences,
            'non_ascii_ratio': non_ascii_ratio,
            'doubles_ratio': doubles_ratio,
            'letter_ratio': letter_ratio,
        }

    def extract_words(self, text):
        tokens = nltk.wordpunct_tokenize(text)
        return [token for token in tokens if not re.search('[\W^\d]', token)]

    def average_word_length(self, words):
        words_len = len(words)
        return sum(len(word) for word in words) / words_len if words_len else 0

    def vowel_ratio(self, words):
        vowels_count = 0
        for word in words:
            vowels_count += len(re.findall('[{}]'.format(VOWELS), word))
        vowel_ratio = self.__ratio_in_text(words, vowels_count)
        return vowel_ratio

    def __ratio_in_text(self, words, variable_count):
        words_len = sum(len(word) for word in words)
        return variable_count / words_len

    def average_words_in_sentences(self, words_len, text):
        return words_len / len(nltk.sent_tokenize(text))

    def non_ascii_ratio(self, text):
        non_ascii = len(re.sub('[\x20-\x7e]', '', text))
        return non_ascii / len(text)

    def double_letter_and_vowels_ratio(self, words):
        doubles_letter = 0
        doubles_vowel = 0
        for word in words:
            word = word.lower()
            letter_iterator = iter(word)
            last_letter = next(letter_iterator)
            is_last_vowel = last_letter in VOWELS
            for letter in letter_iterator:
                is_vowel = letter in VOWELS
                if is_last_vowel and is_vowel:
                    doubles_vowel += 1
                is_last_vowel = is_vowel
                if letter == last_letter:
                    doubles_letter += 1
                last_letter = letter
        doubles = {
            'doubles_letters': self.__ratio_in_text(words, doubles_letter),
            'doubles_vowels' : self.__ratio_in_text(words, doubles_vowel),
        }
        return doubles

    def alphabet_ratio(self, words):
        letter_ratio = []
        for letter in LETTERS:
            letter_count = 0
            for word in words:
                lower_case_word = word.lower()
                letter_count += lower_case_word.count(letter)
            letter_ratio.append(self.__ratio_in_text(words, letter_count))
        return letter_ratio
