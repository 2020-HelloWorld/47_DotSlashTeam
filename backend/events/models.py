from django.db import models
from home.models import club,student
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    date = models.DateField()
    club = models.ForeignKey(club,on_delete=models.CASCADE)
    details =  models.CharField(max_length=250)

class participant(models.Model):
    id = models.AutoField(primary_key=True)
    srn = models.ForeignKey(student,on_delete=models.CASCADE)
    event = models.ForeignKey(event,on_delete=models.SET_NULL, null=True, default=None, related_name='participants')
    details = models.CharField(max_length=500,null=True, default=None)
    proof = models.ImageField(upload_to="uploads",null=True, default=None)
    signed = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)],null=True,default=None)
    
class winner(models.Model):
    id = models.OneToOneField(participant,primary_key=True,on_delete=models.CASCADE)
    position = models.IntegerField(null=False)
    
class report(models.Model):
    id = models.AutoField(primary_key=True)
    details = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="uploads")
    event = models.ForeignKey(event,on_delete=models.CASCADE)  

class organizer(models.Model):
    id = models.AutoField(primary_key=True)
    srn = models.ForeignKey(student,on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    event = models.ForeignKey(event,on_delete=models.CASCADE)  

    
    
    
    