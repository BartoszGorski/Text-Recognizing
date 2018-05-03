import wikipedia
import re


class ArticleGetter:
    def __get_random_page(self, language):
        wikipedia.set_lang(language)
        title = wikipedia.random()
        try:
            return self.__get_page(title)
        except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
            return self.__get_random_page(language)

    def __get_page(self, title):
        return wikipedia.page(title)

    def __chop_summary(self, summary):
        return summary.split("\n\n")[0]

    def __remove_non_words(self, text):
        return re.sub(r'[^A-Za-zĄ-ż\'\. ]', '', text)

    def __remove_newlines(self, text):
        return text.replace('\n', ' ')

    def __remove_manyspaces(self, text):
        return re.sub(r'\s+', ' ', text)

    def clear_text(self, text):
        text = self.__remove_non_words(text)
        text = self.__remove_newlines(text)
        text = self.__remove_manyspaces(text)
        return text

    def get_article(self, language='en', shortest_summary=500):
        cleared_text = ""
        page_not_found = True
        while page_not_found:
            page = self.__get_random_page(language)
            summary = self.__chop_summary(page.summary)
            if len(summary) < shortest_summary:
                continue
            page_not_found = False
            cleared_text = self.clear_text(summary)
        return cleared_text

