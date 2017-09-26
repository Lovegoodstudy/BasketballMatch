#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import csv
import random

csvFile = open("data/matchDataTrain.csv", "r")
reader = csv.reader(csvFile)

#get win and lose from string
def getWinAndLose(str):
    number = '0123456789'
    flag = True  #flag to find win or lose
    win = ''
    lose = ''
    for char in str:
        if char in number:
            if flag:
                win = win + char
            else:
                lose = lose + char
        else:
            flag = False
    return win, lose

#translate origin data from csv to array data
def translateMatchOriginData(matchOriginData):
    matchData = []
    matchData.append(matchOriginData[0])  # AwayTeam Name
    matchData.append(matchOriginData[1])  # AtHomeTeam Name

    win, lose = getWinAndLose(matchOriginData[2])  # AwayTeam Match Data
    matchData.append(win)
    matchData.append(lose)

    win, lose = getWinAndLose(matchOriginData[3])  # AtHomeTeam Match Data
    matchData.append(win)
    matchData.append(lose)

    matchData.append(matchOriginData[4].split(':')[0])  # AwayTeam Result
    matchData.append(matchOriginData[4].split(':')[1])  # AtHomeTeam Result

    return matchData

#get all data into array
def getAllMatchData():
    matchDataArray = []
    reader.next()  #Skip Line 1
    for matchOriginData in reader:
        matchData = translateMatchOriginData(matchOriginData)
        matchDataArray.append(matchData)
    return matchDataArray

matchDataArray = getAllMatchData()

#get some random data from array
def getMatchData(number):
    slice = random.sample(matchDataArray, number)
    return slice