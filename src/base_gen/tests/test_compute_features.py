from src.base_gen.BaseGen import BaseGen

SIMPLE_SENTENCE = "Abćńa I'm 125 xz. Ańżss, 5% oo-k3 Ωw-oą ok Lol.."


class TestCalculateFeatures:
    def setup_class(self):
        self.base_gen = BaseGen()
        self.words = self.base_gen.extract_words(SIMPLE_SENTENCE)

    def test_extract_words(self):
        assert len(self.base_gen.extract_words(SIMPLE_SENTENCE)) == 10

    def test_average_word_length(self):
        assert self.base_gen.average_word_length(self.words) == 2.5

    def test_vowel_ratio(self):
        text_vowel_ratio, word_vowel_ratio = self.base_gen.vowel_ratio(self.words)
        assert text_vowel_ratio == 0.36
        assert word_vowel_ratio == 0.9

    def test_average_words_in_sentences(self):
        assert self.base_gen.average_words_in_sentences(len(self.words), SIMPLE_SENTENCE) == 5.0

    def test_nonascii_ratio(self):
        assert self.base_gen.nonascii_ratio(SIMPLE_SENTENCE) == 0.125