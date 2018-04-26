from django.db import models

# Create your models here.


class employees(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.CharField(max_length=50)

    def __str__(self):

        return self.name


