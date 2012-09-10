# tnode.py

from utils import len_comm_prefix
#-----------------------------------------------------------------------------

class tnode(dict):
    '''A node in trie'''

    T = ''  # terminal marker

    def add(self, word):
        '''Add word to this tnode'''
        if word is self.T:
            # word is empty, add ok
            self[self.T] = None
        else:
            v = self._find_splits(word)
            if v is self.T:
                # cannot find prefixes of word, make word a key; add ok
                self[word] = tnode({self.T: None})
            elif word.startswith(v):
                # v is a prefix of word, no need to split v; recurse
                self[v].add(word[len(v):])
            else:
                # replace v with the common prefix of word and v; recurse
                cl = len_comm_prefix(word, v)
                cp,pv = v[:cl], v[cl:]
                oc = self.pop(v)
                self[cp] = tnode({pv: oc})
                self[cp].add(word[cl:])

    def find(self, word):
        '''Return True if word can be found in this tnode'''
        if word is self.T:
            # terminal exists
            return True if self.T in self else False
        else:
            v = self._find_splits(word)
            if v is not self.T and word.startswith(v):
                # recurse iff v is an exact prefix
                return self[v].find(word[len(v):])
            else:
                return False

    def count(self):
        '''Count the number or words in this tnode'''
        s = 0
        for k, v in self.iteritems():
            if k is self.T:
                s += 1
            else:
                s += v.count()
        return s

    def iterwords(self):
        '''Iterator of all words from this node'''
        for k, v in self.iteritems():
            if k is self.T:
                yield self.T
            else:
                for w in v.iterwords():
                    yield k + w

    def words(self):
        '''Return all words from this node in a Python list'''
        return list(self.iterwords())

    def _find_splits(self, word):
        '''
        Find the potential key to split for word.

        @return A key in self whose first character is the same as word;
                self.T if not found.

        '''
        for k in self.iterkeys():
            if k is not self.T and k[0] == word[0]:
                return k

        return self.T
#-----------------------------------------------------------------------------
