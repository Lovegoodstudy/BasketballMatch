import csv

csvFile = open("data/matchDataTrain.csv", "r")
reader = csv.reader(csvFile)
for item in reader:
    print(item)