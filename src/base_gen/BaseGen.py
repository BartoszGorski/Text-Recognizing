from src.base_gen.ArticleGetter import get_random_page

LANGUAGES = ['en', 'pl']
SHORTEST_SUMMARY = 1000



class BaseGen:
    def __init__(self, pages_count_to_get):
        self.pages_count_to_get = pages_count_to_get

    def collect_articles_date(self):
        for language in LANGUAGES:
            for i in range(self.pages_count_to_get):
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
        words = text.split()
        average_word_length = self.__average_word_length(words)

    def __average_word_length(self, words):
        words_len = len(words)
        return sum(len(word) for word in words) / words_len if words_len else 0


