# test_trie.py

import unittest as ut
from trie import trie
#-----------------------------------------------------------------------------

class Test_trie(ut.TestCase):
    def setUp(self):
        self.fname = 'tests/tst/can-30.words'
        self.trie = trie()

    def tearDown(self):
        del self.trie
    
    def test_add(self):
        total = 0
        with open(self.fname) as f:
            for line in f:
                self.trie.add(line.strip())
                total += 1

        self.assertEqual(total, self.trie.count())

    def test_add_duplicate(self):
        ws = ['word'] * 10
        for w in ws:
            self.trie.add(w)

        self.assertEqual(1, self.trie.count())

    def test_iterwords(self):
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

        print self.trie.words(pre)
#-----------------------------------------------------------------------------

