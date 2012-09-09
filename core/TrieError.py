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
