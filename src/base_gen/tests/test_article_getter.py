from .test_compute_features import SIMPLE_SENTENCE
from ..ArticleGetter import ArticleGetter


def test_clear_text():
    ag = ArticleGetter()
    text = ag.clear_text(SIMPLE_SENTENCE)
    assert text == "Abćńa I'm xz. Ańżss ook woą ok Llo.."
