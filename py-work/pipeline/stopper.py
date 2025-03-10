#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk

_stop_words = set(nltk.corpus.stopwords.words("turkish"))
_stop_words.update([""])
_stop_words.update(["olan", "bir", "aşağı", "hangi", "şimdi", "şöyle", "böyle"])
_stop_words.update(["tamam", "iyi", "ta", "mı", "mi", "ol", "yap", "et"])

def is_stop(word):
    if word in _stop_words:
        return True
    if len(word) <= 1:
        return True
    return False

def remove_stops(tokens):
    return [token for token in tokens if not is_stop(token)]