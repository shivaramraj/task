from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Trains(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    TrainName=models.CharField(max_length=100)
    TrainNo=models.IntegerField()
    From_To=models.CharField(max_length=100)
    No_of_Coaches=models.IntegerField()
    TrainImage=models.ImageField()

    def __str__(self):
        return self.TrainName
        
