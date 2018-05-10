from src.utils.FeaturesGen import FeaturesGen

SIMPLE_SENTENCE = "Abćńa I'm 125 xz. Ańżss, 5% oo-k3 Ωw-oą ok Llo.."


class TestCalculateFeatures:
    def setup_class(self):
        self.features_gen = FeaturesGen()
        self.words = self.features_gen.extract_tokens(SIMPLE_SENTENCE)
        self.sum_word_length = sum(len(word) for word in self.words)
        self.characters_count = len(SIMPLE_SENTENCE)
        self.tokens_count = len(self.features_gen.extract_tokens(SIMPLE_SENTENCE))

    def test_extract_words(self):
        assert len(self.features_gen.extract_tokens(SIMPLE_SENTENCE)) == 20

    def test_average_word_length(self):
        assert self.features_gen.average_word_length(self.words) == self.sum_word_length / self.tokens_count

    def test_vowel_ratio(self):
        vowel_ratio = self.features_gen.vowel_ratio(SIMPLE_SENTENCE)
        assert vowel_ratio == 9 / self.characters_count

    def test_non_ascii_ratio(self):
        assert self.features_gen.non_ascii_ratio(SIMPLE_SENTENCE) == 6 / len(SIMPLE_SENTENCE)

    def test_double_letters_and_vowels(self):
        doubles = self.features_gen.double_letter_and_vowels_ratio(SIMPLE_SENTENCE)
        assert doubles[0] == 4 / self.characters_count
        assert doubles[1] == 3 / self.characters_count
        assert doubles[2] == 1 / self.characters_count

    def test_alphabet_ratio(self):
        letter_ratio = self.features_gen.alphabet_ratio(SIMPLE_SENTENCE)
        assert letter_ratio[0] == 3 / self.characters_count
        assert letter_ratio[24] == 0 / self.characters_count
        assert letter_ratio[8] == 1 / self.characters_count
        assert letter_ratio[11] == 2 / self.characters_count

    def test_spaces_ratio(self):
        spaces_ratio = self.features_gen.spaces_ratio(SIMPLE_SENTENCE)
        assert spaces_ratio == 9 / self.characters_count
