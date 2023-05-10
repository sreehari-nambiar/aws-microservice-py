import wikipedia
from textblob import TextBlob


def wiki(name="War Goodness", length=1):
    """
    This is a Wikipedia Fetcher
    """
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """
    Search Wikipedia for Names
    """
    results = wikipedia.search(name)
    return results


def phrase(name):
    """
    Returns from Wikipedia
    """
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
