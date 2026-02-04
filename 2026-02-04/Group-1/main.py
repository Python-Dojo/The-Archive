"""
Given a set of documents and a search term
Filter and order the documents using TF-IDF

Term Frequency = (The number of times a term appears in the document) / (total number of terms in the document)
Inverse Document Frequency = log((Total number of documents)/(Number of documents that contain the term))_
TF-IDF = TF x IDF
"""

import math
import re
import sys
from collections import defaultdict
from operator import itemgetter
from typing import Iterable

import requests

DOCUMENT_URLS = [
    "https://raw.githubusercontent.com/pola-rs/polars/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/immich-app/immich/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/astral-sh/uv/refs/heads/main/README.md",
    "https://raw.githubusercontent.com/HypothesisWorks/hypothesis/refs/heads/master/README.md",
    "https://raw.githubusercontent.com/astral-sh/ruff/refs/heads/main/README.md",
]


def generate_corpus(urls: list[str]) -> dict[str, dict[str, int]]:
    """Given a list of urls, return dictionary of the documents each with dictionaries of their tokens and frquencies."""
    corpus_dictionary = {}
    for url in urls:
        document_string = read_document(url)
        document_tokens = get_tokens(document_string)
        token_frequency = defaultdict(int)
        for token in document_tokens:
            token_frequency[token] += 1
        corpus_dictionary[url] = token_frequency
    return corpus_dictionary


def get_tokens(document: str) -> list[str]:
    return re.sub(r"[^a-z ]", "", document.lower()).split()


def read_document(url: str) -> str:
    return str(requests.get(url).content)


def term_frequency(term_counts: dict[str, int], term: str) -> float:
    return term_counts[term] / sum(term_counts.values())


def inverse_document_frequency(corpus: dict[str, dict[str, int]], term: str) -> float:
    containing = sum(1 for term_counts in corpus.values() if term_counts.get(term, 0) > 0)
    return math.log((len(corpus) + 1) / (containing + 1))


def find_terms(terms: Iterable[str]) -> Iterable[tuple[str, float]]:
    """Return documents that contain the term ordered via TF-IDF"""
    corpus = generate_corpus(DOCUMENT_URLS)
    scores = {
        url: sum(
            term_frequency(term_counts, term) * inverse_document_frequency(corpus, term)
            for term in map(str.lower, terms)
        )
        for url, term_counts in corpus.items()
    }
    return sorted(scores.items(), key=itemgetter(1), reverse=True)

if "__main__" == __name__:
    terms = sys.argv[1:]
    for url, score in find_terms(terms):
        print(f"{score=} - {url=}")
