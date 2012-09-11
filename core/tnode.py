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

    def iterwords(self, prefix = ''):
        '''
        Iterator of all words starting with prefix in this node.

        @param prefix: if not given, prefix is default to '' because all
                       Python strings startswith '', and iterwords will
                       iterate through all words.
        
        '''
        if prefix is self.T:
            for k, v in self.iteritems():
                if k is self.T:
                    yield self.T
                else:
                    for w in v.iterwords():
                        yield k + w
        else:
            s = self._find_splits(prefix)
            if s is self.T:
                return
            if s.startswith(prefix):
                for w in self[s].iterwords():
                    yield s + w
            elif prefix.startswith(s):
                for w in self[s].iterwords(prefix[len(s):]):
                    yield s + w

    def words(self, prefix = ''):
        '''
        Return all words starting with prefix in this node as a Python
        list.

        @param prefix: if not given, prefix is default to '' because all
                       Python strings startswith '', and iterwords will
                       iterate through all words.
        
        ''' 
        return list(self.iterwords(prefix))

    def __str__(self, d = 0):
        '''
        Trie formatted as a tree.

        End of words are marked by '$' so as to identify internal nodes which
        are also valid words.
        '''
        r = ''
        pre = '' if d == 0 else (' '*(d-1) + '|')
        for k, v in self.iteritems():
            if k is not self.T:
                r += pre + (k)
                if self.T in v:
                    r += '$'
                r += '\n'
                r += v.__str__(d + 1)
        return r

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
