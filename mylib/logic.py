import wikipedia


def wiki(name="War Goodness", length=1):
    """
    This is a Wikipedia Fetcher
    """
    my_wiki = wikipedia.summary(name, length)
    return my_wiki
