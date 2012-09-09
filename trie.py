# trie.py

from core.tnode import tnode
from core.TrieError import DuplicateWord
#-----------------------------------------------------------------------------

class trie(object):
    '''The trie class'''
    def __init__(self):
        self._root = tnode()

    def add(self, word):
        '''Add word to the trie'''
        if self.find(word):
            raise DuplicateWord(word)
        else:
            self._root.add(word)

    def find(self, word):
        '''Return True if word is in the trie'''
        return self._root.find(word)

    def count(self):
        '''The total number of words in the trie'''
        return self._root.count()
#-----------------------------------------------------------------------------

