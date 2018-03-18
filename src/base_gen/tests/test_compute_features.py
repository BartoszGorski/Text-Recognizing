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
        vowel_ratio = self.base_gen.vowel_ratio(self.words)
        assert vowel_ratio == 9 / 25

    def test_average_words_in_sentences(self):
        assert self.base_gen.average_words_in_sentences(len(self.words), SIMPLE_SENTENCE) == 10 / 2

    def test_non_ascii_ratio(self):
        assert self.base_gen.non_ascii_ratio(SIMPLE_SENTENCE) == 6 / len(SIMPLE_SENTENCE)

    def test_double_letters_and_vowels(self):
        doubles = self.base_gen.double_letter_and_vowels_ratio(self.words)
        assert doubles['doubles_letters'] == 3 / 25
        assert doubles['doubles_vowels']  == 1 / 25

    def test_alphabet_ratio(self):
        letter_ratio = self.base_gen.alphabet_ratio(self.words)
        assert letter_ratio[0] == 3 / 25
        assert letter_ratio[24] == 0 / 25
        assert letter_ratio[8] == 1 / 25
        assert letter_ratio[11] == 2 / 25

    def test_clear_text(self):
        text = self.base_gen.clear_text(SIMPLE_SENTENCE)
        assert text == "Abćńa I'm xz. Ańżss ook woą ok Llo.."
