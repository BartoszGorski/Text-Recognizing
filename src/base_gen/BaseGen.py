from src.base_gen.ArticleGetter import get_random_page

LANGUAGES = ['en', 'pl']


class BaseGen:
    def __init__(self, pages_count_to_get):
        self.pages_count_to_get = pages_count_to_get

    def collect_articles_date(self):
        for language in LANGUAGES:
            for i in range(self.pages_count_to_get):
                page = get_random_page(language)
