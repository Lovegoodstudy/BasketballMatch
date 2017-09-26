#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest
import matchDataInit

class TestMatchDataInit(unittest.TestCase):

    def test_getWinAndLose(self):
        self.assertEqual(matchDataInit.getWinAndLose('132胜7负'), ('132', '7'))

    def test_translateMatchOriginData(self):
        self.assertEqual(matchDataInit.translateMatchOriginData(['143', '11', '132胜7负', '7胜78负', '123:78']), ['143', '11', '132', '7', '7', '78', '123', '78'])

    def test_getMatchData(self):
        self.assertEqual(len(matchDataInit.matchDataArray), 7084)
        self.assertEqual(len(matchDataInit.getMatchData(100)), 100)

if __name__ == '__main__':
    unittest.main()