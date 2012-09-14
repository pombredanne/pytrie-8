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

    def rm(self, word):
        '''Remove word from the trie'''
        self._root.rm(word)

    def find(self, word):
        '''Return True if word is in the trie'''
        return self._root.find(word)

    def count_words(self):
        '''The total number of words in the trie'''
        return self._root.count_words()

    def count_tnode(self):
        '''The total number of tnodes in the trie'''
        return self._root.count_tnode()

    def iterwords(self, prefix = ''):
        '''
        Iterator of all the words starting with prefix lexicographically.

        @param prefix: if not given, prefix is default to '' because all
                       Python strings startswith '', and iterwords will
                       iterate through all words.
        
        '''
        return self._root.iterwords(prefix)

    def words(self, prefix = ''):
        '''
        Return all words starting with prefix lexicographically as a Python
        list.
        
        @param prefix: if not given, prefix is default to '' because all
                       Python strings startswith '', and iterwords will
                       iterate through all words.
        
        '''
        return self._root.words(prefix)

    def __str__(self):
        return str(self._root)
#-----------------------------------------------------------------------------

