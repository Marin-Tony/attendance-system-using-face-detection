       
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
    
    #def __str__(self):
     #   return self.designation

class Present(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	present=models.BooleanField(default=False)


class Time(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.ForeignKey(desig,on_delete=models.CASCADE,null=True,default=2)
    date = models.DateField(default=datetime.date.today)
    time=models.DateTimeField(null=True,blank=True)
    out=models.BooleanField(default=False)
    #designation=models.ForeignKey(desig,on_delete=models.CASCADE)

class staff_mesg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(max_length=500)

class Notify(models.Model):
    notification=models.TextField(max_length=500,default=" ")

class course_details(models.Model):
    course_name = models.TextField(verbose_name='Course Name', max_length=50,null=False)
    Eligibility = models.TextField(max_length=30,null=False)
    semester = models.TextField(verbose_name='No.of Semsesters:',max_length=3,null=False)
    Duration = models.TextField(max_length=10,null=False)

class faculty_details(models.Model):
     Name = models.TextField(max_length=30,null=False)
     Qualification = models.TextField(max_length=30,null=False)
     Department = models.TextField(max_length=30,null=False)
     position = models.TextField(max_length=30,null=False)
     date_of_joining = models.DateField(default=datetime.date.today)

class add_marks(models.Model):
    Student_name =  models.TextField(max_length=30,null=False)
    Subject = models.TextField(max_length=20,null=False)
    Marks = models.IntegerField(null=False)
    Total = models.IntegerField(verbose_name='Total Marks',null=False)

class add_remarks(models.Model):
    Student_name =  models.TextField(max_length=30,null=False)
    Remarks = models.TextField(max_length=500,null=False)


