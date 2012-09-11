# trie.py

from core.tnode import tnode
#-----------------------------------------------------------------------------

class trie(object):
    '''The trie class'''
    def __init__(self):
        self._root = tnode()

    def add(self, word):
        '''Add word to the trie'''
        self._root.add(word)

    def find(self, word):
        '''Return True if word is in the trie'''
        return self._root.find(word)

    def count(self):
        '''The total number of words in the trie'''
        return self._root.count()

    def iterwords(self, prefix = ''):
        '''
        Iterator of all the words starting with prefix.

        @param prefix: default to '' because all Python string starts with ''

        '''
        return self._root.iterwords(prefix)

    def words(self, prefix = ''):
        '''
        Return all words starting with prefix as a Python list.

        @param prefix: default to '' because all Python string starts with ''

        '''
        return self._root.words(prefix)
#-----------------------------------------------------------------------------

