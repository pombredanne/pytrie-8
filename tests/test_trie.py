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

#-----------------------------------------------------------------------------

