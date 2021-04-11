from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from users.models import staff_mesg,desig,Notify,Time,Present

	
DESIGNATION_CHOICES=[('teacher','Teacher'),('parent_student','Parent_Student'),('staff','Staff')]
#SUBJECT_CHOICES=[('dbms','DBMS'),('sql','SQL'),('python','Python'),('java','Java'),('maths','Maths'),('aws','AWS')]

class checkForm(forms.Form):
	username=forms.CharField(max_length=30)
	notification=forms.CharField(widget=forms.Textarea(),label='Notification')
	class Meta:
		model = Notify
		fields=['username','notification']
	

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

class DateForm_2(forms.Form):
	date_from=forms.DateField(label='Date:',widget = forms.SplitDateTimeWidget(date_format=datetime.now()))


	
       