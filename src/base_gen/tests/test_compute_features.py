from src.base_gen.BaseGen import BaseGen

SIMPLE_SENTENCE = "Abćńa I'm 125 xz. Ańżss, 5% oo-k3 Ωw-oą ok Llo.."


class TestCalculateFeatures:
    def setup_class(self):
        self.base_gen = BaseGen()
        self.words = self.base_gen.extract_words(SIMPLE_SENTENCE)

    def test_extract_words(self):
        assert len(self.base_gen.extract_words(SIMPLE_SENTENCE)) == 10

    def test_average_word_length(self):
        assert self.base_gen.average_word_length(self.words) == 25 / 10

    def test_vowel_ratio(self):
        text_vowel_ratio, word_vowel_ratio = self.base_gen.vowel_ratio(self.words)
        assert text_vowel_ratio == 9 / 25
        assert word_vowel_ratio == 9 / 10

    def test_average_words_in_sentences(self):
        assert self.base_gen.average_words_in_sentences(len(self.words), SIMPLE_SENTENCE) == 10 / 2

    def test_non_ascii_ratio(self):
        assert self.base_gen.non_ascii_ratio(SIMPLE_SENTENCE) == 6 / len(SIMPLE_SENTENCE)

    def test_double_letters_and_vowels(self):
        doubles = self.base_gen.double_letter_and_vowels_ratio(self.words)
        assert doubles['text_doubles_letters'] == 3 / 25
        assert doubles['text_doubles_vowels']  == 1 / 25
        assert doubles['word_doubles_letters'] == 3 / 10
        assert doubles['word_doubles_vowels']  == 1 / 10

    def test_alphabet_ratio(self):
        text_letter_ratio, word_letter_ratio = self.base_gen.alphabet_ratio(self.words)
        assert text_letter_ratio['a'] == 3 / 25
        assert text_letter_ratio['y'] == 0 / 25
        assert text_letter_ratio['i'] == 1 / 25
        assert text_letter_ratio['l'] == 2 / 25
        assert word_letter_ratio['a'] == 3 / 10
        assert word_letter_ratio['y'] == 0 / 10
        assert word_letter_ratio['i'] == 1 / 10
        assert word_letter_ratio['l'] == 2 / 10
