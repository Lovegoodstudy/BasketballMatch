#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import unittest
import matchDataInit
import teamDataInit

#test for matchDataInit.py
class TestMatchDataInit(unittest.TestCase):

    def test_getWinAndLose(self):
        self.assertEqual(matchDataInit.getWinAndLose('132胜7负'), ('132', '7'))

    def test_translateMatchOriginData(self):
        self.assertEqual(matchDataInit.translateMatchOriginData(['143', '11', '132胜7负', '7胜78负', '123:78']), ['143', '11', '132', '7', '7', '78', '123', '78'])

    def test_getMatchData(self):
        self.assertEqual(len(matchDataInit.getAllMatchData()), 7084)

class TestTeamDataInit(unittest.TestCase):

    def test_translateTeamOriginData(self):
        self.assertEqual(teamDataInit.translateTeamOriginData(['207', '15', '19', '0', '6.5', '62.50%', '0.5', '0.8', '', '0', '0', '62.50%', '0.3', '0.4', '1.6', '0.4', '1.2', '0.2', '0.1', '0.3', '0.2', '0.6', '1.3']), ['207', '15', '0', '19', '6.5', '0.5', '0.8', '0', '0', '0.3', '0.4', '1.6', '0.4', '1.2', '0.2', '0.1', '0.3', '0.2', '0.6', '1.3'])

    def test_getTeamData(self):
        self.assertEqual(len(teamDataInit.getAllTeamData()), 3732)

if __name__ == '__main__':
    unittest.main()