import re
import nltk
nltk.download('punkt')

from src.base_gen.ArticleGetter import get_random_page

LANGUAGES = ['en', 'pl']
SHORTEST_SUMMARY = 1000
VOWELS = 'aeiouyAEIOUY'


class BaseGen:

    def collect_articles_date(self, pages_count_to_get):
        for language in LANGUAGES:
            for i in range(pages_count_to_get):
                page = get_random_page(language)
                summary = self.__chop_summary(page.summary)
                if len(summary) < SHORTEST_SUMMARY:
                    continue
                p_id = page.pageid
                analysed = self.__analyse_text(summary)

    def __chop_summary(self, summary):
        return summary.split("\n\n")[0]

    def __analyse_text(self, text):
        # type: (str) -> dict[str, float | list]

        average_word_length = self.__average_word_length(text)
        vowel_ratio = self.__vowel_ratio(text)
        average_words_in_sentences = self.__average_words_in_sentences(text)

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
        sentence_vowel_ratio = self.__vowel_ratio_in_sentence(words, vowels_count)
        word_vowel_ratio = self.__vowel_ratio_per_word(len(words), vowels_count)
        return sentence_vowel_ratio, word_vowel_ratio

    def __vowel_ratio_in_sentence(self, words, vowels_count):
        words_len = sum(len(word) for word in words)
        return vowels_count / words_len

    def __vowel_ratio_per_word(self, words_count, vowels_count):
        return vowels_count / words_count

    def average_words_in_sentences(self, words_len, text):
        return words_len / len(nltk.sent_tokenize(text))
