#ingest shots

import csv
#path=raw_input("Full file Path: ")
path="F:\django\sTrack\shots.csv"

count=0
with open(path,"r") as csvFile:
    readCSV=csv.reader(csvFile, delimiter=",")
    for line in readCSV:
        if count!=0:
            
            print (line[0])
            print (line[1])
            print (line[2])

        count=count+1
    
