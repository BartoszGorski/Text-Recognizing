from src.base_gen.BaseGen import BaseGen

EN_SENTENCE = """
That guy run like a jaguar-rabbit... 
Man was like 70 years old but could do a back flip, drop into the splits, and come up running. 
He's awesome.
 """
PL_SENTENCE = """
Koleś był jak jaguaro-zając...
Miał 70 lat, ale potrafił zrobić salto do tyłu, szpagat, i nadal biec.
Jest świetny.
"""


class TestCalculateFeatures:
    def setup_class(self):
        self.base_gen = BaseGen()

    def test_average_word_length(self):
        assert self.base_gen.average_word_length(EN_SENTENCE) == 0
        assert self.base_gen.average_word_length(PL_SENTENCE) == 0

    def test_vowel_ratio(self):
        assert self.base_gen.vowel_ratio(EN_SENTENCE) == 0
        assert self.base_gen.vowel_ratio(PL_SENTENCE) == 0

    def test_average_words_in_sentences(self):
        assert self.base_gen.average_words_in_sentences(EN_SENTENCE) == 0
        assert self.base_gen.average_words_in_sentences(PL_SENTENCE) == 0
