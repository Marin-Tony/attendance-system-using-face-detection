from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from users.models import staff_mesg,desig,Notify,Time,Present,faculty_details,course_details,add_marks,add_remarks

GEEKS_CHOICES =((1,"Teacher"),(2,"Parent_Student"),(3,"Staff"))
DESIGNATION_CHOICES=[('teacher','Teacher'),('parent_student','Parent_Student'),('staff','Staff')]

class checkForm(forms.ModelForm):
	
	notification=forms.CharField(widget=forms.Textarea(),label='Notification')
	class Meta:
		model = Notify
		fields=['notification']
	

class TextAreaForm(forms.ModelForm):
	username=forms.CharField(label='Username:',max_length=30)
	message=forms.CharField(widget=forms.Textarea(),label='Message')
	class Meta:
		model = staff_mesg
		fields=['username','message']
	

class DateForm(forms.Form):
	date=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))


class UsernameAndDateForm(forms.ModelForm):
	username=forms.CharField(label='Username:',max_length=30)
	designation= forms.ChoiceField(label='Designation:',required=True,choices=DESIGNATION_CHOICES)
	class Meta:
		model = desig
		fields = ['username','designation']

class courseForm(forms.ModelForm):
	course_name=forms.CharField(label='Course Name',max_length=50)
	Eligibility = forms.CharField(max_length=30)
	semester = forms.CharField(max_length=3)
	Duration= forms.CharField(max_length=10)
	class Meta:
		model = course_details
		fields = ['course_name','Eligibility','semester','Duration']

class facultyForm(forms.ModelForm):
	Name = forms.CharField(max_length=30)
	Qualification = forms.CharField(max_length=30)
	Department = forms.CharField(max_length=30)
	position = forms.CharField(max_length=30)
	date_of_joining = forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))

	class Meta:
		model = faculty_details
		fields = ['Name','Qualification','Department','position','date_of_joining']
       
class marksForm(forms.ModelForm):
	Student_name = forms.CharField(max_length=30,label='Student Name')
	Subject = forms.CharField(max_length=20)
	Marks = forms.IntegerField()
	Total = forms.IntegerField()
	class Meta:
		model = add_marks
		fields = ['Student_name','Subject','Marks','Total']
class remarksForm(forms.ModelForm):
	Student_name = forms.CharField(max_length=30,label='Student Name')
	Remarks = forms.CharField(widget=forms.Textarea())
	class Meta:
		model = add_remarks
		fields = ['Student_name','Remarks']
