# test_trie.py

import os
import unittest as ut
from random import randint
from trie import trie
#-----------------------------------------------------------------------------

class Test_trie(ut.TestCase):
    def setUp(self):
        self.fname = 'tests/tst/can-30.words'
        self.trie = trie()

    def tearDown(self):
        del self.trie
    
    def test_init(self):
        self.assertEqual(0, self.trie.count_words())
        self.assertEqual(1, self.trie.count_tnode())

    def test_add(self):
        '''Add words'''
        total = 0
        with open(self.fname) as f:
            for line in f:
                self.trie.add(line.strip())
                total += 1

        self.assertEqual(total, self.trie.count_words())

    def test_add_duplicate(self):
        '''Add duplicate words'''
        ws = ['word'] * 10
        for w in ws:
            self.trie.add(w)

        self.assertEqual(1, self.trie.count_words())

    def test_rm(self):
        '''Remove words'''
        s = set()
        with open(self.fname) as f:
            for line in f:
                self.trie.add(line.strip())
                s.add(line.strip())
        
        for w in s:
            self.trie.rm(w)

        self.assertEqual(0, self.trie.count_words())
        self.assertEqual(1, self.trie.count_tnode())
        
    def test_iterwords(self):
        '''Traversing all words'''
        s = set()
        with open(self.fname) as f:
            for line in f:
                self.trie.add(line.strip())
                s.add(line.strip())

        for w in self.trie.iterwords():
            self.assertTrue(w in s)

        for w in self.trie.words():
            self.assertTrue(w in s)

    def test_iterwords_prefix(self):
        '''Traversing words with a prefix'''
        pre = 'tr'
        s = set()
        with open(self.fname) as f:
            for line in f:
                w = line.strip()
                self.trie.add(w)
                if w.startswith(pre):
                    s.add(w)

        for w in self.trie.iterwords(pre):
            self.assertTrue(w in s)

        self.assertEqual(len(s), len(self.trie.words(pre)))

        # use other streams to see the actual print out
        with open(os.devnull,"w") as f:
            print >> f, self.trie

    def test_print(self):
        '''Printing a trie'''
        # add roughly 1/200
        with open(self.fname) as f:
            for line in f:
                w = line.strip()
                if 1 == randint(1, 200):
                    self.trie.add(w)
        # use other streams to see the actual print out
        with open(os.devnull,"w") as f:
            print >> f, self.trie

    def test_print2(self):
        '''Having an itermediate node as a complete word'''
        self.trie.add('act')
        self.trie.add('action')
        # use other streams to see the actual print out
        with open(os.devnull,"w") as f:
            print >> f, self.trie

#-----------------------------------------------------------------------------

