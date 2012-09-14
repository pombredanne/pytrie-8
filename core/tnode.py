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

    def rm(self, word):
        '''Remove word from this tnode'''
        if word is self.T:
            if self.T in self:
                del self[self.T]
                return True
            else:
                return False
        else:
            v = self._find_splits(word)
            if v is not self.T and word.startswith(v):
                # recurse iff v is an exact prefix
                vc = self[v]
                if vc is None:
                    print word, v, vc, super(tnode, self).keys()
                success = vc.rm(word[len(v):])
                if success:
                    # take out this prefix if it has no children 
                    if len(vc) == 0:
                        del self[v]
                    # merge this prefix with its only non-terminal children
                    elif len(vc) == 1 and self.T not in vc:
                        s, oc = vc.popitem()
                        del self[v]
                        self[v + s] = oc
                return success

            return False

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

    def count_words(self):
        '''Count the number or words in this tnode'''
        return sum(1 if k is self.T else v.count_words()
                   for k, v in self.iteritems())

    def count_tnode(self):
        '''Count the number of tnode from this tnode'''
        return (1 +
                sum(v.count_tnode()
                    for k, v in self.iteritems()
                    if k is not self.T))

    def iterwords(self, prefix = ''):
        '''
        Iterator of all words starting with prefix lexicographically in this
        node.
        
        @param prefix: if not given, prefix is default to '' because all
                       Python strings "startswith" '', and iterwords will
                       iterate through all words.
        
        '''
        for k in sorted(self.iterkeys()):
            if k.startswith(prefix):
                # this handles prefix == ''
                if k is self.T:
                    yield self.T
                else:
                    for w in self[k].iterwords():
                        yield k + w
            elif prefix.startswith(k):
                # recurse with reduced prefix
                for w in self[k].iterwords(prefix[len(k):]):
                    yield k + w
                    
    def words(self, prefix = ''):
        '''
        All words starting with prefix lexicographically in this node in a
        Python list.
        
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
        pre += '{}{}\n'
        for k in sorted(self.iterkeys()):
            if k is not self.T:
                v = self[k]
                r += pre.format(k, '$' if self.T in v else '')
                r += v.__str__(d + 1)
        return r

    def _find_splits(self, word):
        '''
        Find the potential key to split for word.

        @return self.T if no split point can be found

        '''
        for k in self.iterkeys():
            if k is not self.T and k[0] == word[0]:
                return k

        return self.T
        
#-----------------------------------------------------------------------------
