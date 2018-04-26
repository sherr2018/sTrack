from shots.models import status,shots
import csv

def ingestStatus():
    with open('status.txt', 'r') as r:
        for line in r:
            a=status(status=(line[:-1]))
            a.save()


def shotsIngest():
    path="F:\django\sTrack\shots.csv"
    count=0
    with open(path,"r") as csvFile:
        readCSV=csv.reader(csvFile, delimiter=",")
        for line in readCSV:
            if count!=0:
                s=shots(shotName=line[0],projectCode=line[1],reel=line[2],seq=line[3],clientCode=line[4],sourceStatus=line[5],sourceType=line[6],shotStatus=line[7],rotoStatus=line[8],cpStatus=line[9],clientid=line[10],clientFFrame=line[11],clientLFrame=line[12],clientFrames=line[13],activeFFrame=line[14],activeLFrame=line[15],activeFrames=line[16])
                s.save()
            count=count+1
