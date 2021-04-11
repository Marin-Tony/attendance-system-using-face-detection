       
from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
class desig(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Teacher='teacher'
    Parent_Student='parent_student'
    Staff='staff'
    DESIGNATION_CHOICES=[('teacher','Teacher'),('parent_student','Parent_Student'),('staff','Staff')]
    designation=models.CharField(max_length=30,choices=DESIGNATION_CHOICES,default='parent_student')
    

class Present(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	present=models.BooleanField(default=False)


class Time(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.ForeignKey(desig,on_delete=models.CASCADE,null=True)
    date = models.DateField(default=datetime.date.today)
    time=models.DateTimeField(null=True,blank=True)
    out=models.BooleanField(default=False)
    #designation=models.ForeignKey(desig,on_delete=models.CASCADE)

class staff_mesg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length=500)

class Notify(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    notication=models.TextField(max_length=500)
