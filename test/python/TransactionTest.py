# -*- coding: utf-8 -*-

import unittest
import operator

from ledger import *
from datetime import *

class JournalTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        close_journal_files()

    def test_(self):
        pass
 
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(JournalTestCase)

if __name__ == '__main__':
    unittest.main()
