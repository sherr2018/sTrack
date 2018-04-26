from django.db import models

# Create your models here.

class shots(models.Model):
    shotName=models.CharField(max_length=20)
    projectCode=models.CharField(max_length=20)
    reel=models.CharField(max_length=10)
    seq=models.CharField(max_length=10)
    clientCode=models.CharField(max_length=20)
    sourceStatus=models.CharField(max_length=20)
    sourceType=models.CharField(max_length=20)
    shotStatus=models.CharField(max_length=20)
    rotoStatus=models.CharField(max_length=20)
    cpStatus=models.CharField(max_length=20)
    clientid=models.CharField(max_length=20)
    clientFFrame=models.IntegerField(11)
    clientLFrame=models.IntegerField(11)
    clientFrames=models.IntegerField(11)
    activeFFrame=models.IntegerField(11)
    activeLFrame=models.IntegerField(11)
    activeFrames=models.IntegerField(11)

    def __str__(self):
        return self.shotName

class status(models.Model):
    status=models.CharField(max_length=30)
    def __str__(self):
        return self.status




