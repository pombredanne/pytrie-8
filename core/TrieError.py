# Copyright (c) 2012 Jiaxing Song
# released under the MIT License, see LICENSE for details
# TrieError.py

#-----------------------------------------------------------------------------

class TrieError(Exception):
    '''Base class for trie errors'''
    pass

class DuplicateWord(TrieError):
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return '{} already exists'.format(self.word)
#-----------------------------------------------------------------------------
