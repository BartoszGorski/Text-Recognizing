import wikipedia


def get_random_page(language):
    wikipedia.set_lang(language)
    title = wikipedia.random()

    try:
        return get_page(title)
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
        return get_random_page(language)


def get_page(title):
    return wikipedia.page(title)
