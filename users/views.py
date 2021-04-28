#from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from recognition.forms import checkForm,courseForm,facultyForm,marksForm,remarksForm
from .models import Notify,desig,add_marks,add_remarks,Time,Present
from django.contrib.auth.models import User
import datetime
from recognition.views import hours_vs_date_given_employee
# Create your views here.


@login_required
def register(request):
	print(request.user.username)
	if request.user.username!='admin':
		return render(request,'recognition/dashboard.html')
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save() ###add user to database
			messages.success(request, f'Registered successfully!')
			return redirect('dashboard')
	else:
		form=UserCreationForm()
	return render(request,'users/register.html', {'form' : form})
	if request.user.username!='admin':
		return render(request,'recognition/employee_dashboard.html')

def staff_register(request):
	
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		stf_us = User.objects.get(username=username)
		print(stf_us,stf_us.id)
		des = stf_us.id
		stf_des = desig.objects.get(user_id=des)
		print(stf_des,stf_des.designation)
		stf_desig = stf_des.designation
		if stf_desig == 'staff':
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				# Redirect to a success page.
				return render(request,'recognition/staff_dashboard.html')
			else:
				# Return an 'invalid login' error message.
				return render(request,'recognition/staff_dashboard.html')
		else:
			return render(request,'recognition/Four_login.html')
	else:
		form=AuthenticationForm()
	return render(request,'users/loginstaff.html', {'form' : form})
	

def teacheregister(request):
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		tchr_us = User.objects.get(username=username)
		print(tchr_us,tchr_us.id)
		des = tchr_us.id
		tchr_des = desig.objects.get(user_id=des)
		print(tchr_des,tchr_des.designation)
		tchr_desig = tchr_des.designation
		if tchr_desig == 'teacher':
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				# Redirect to a success page.
				return render(request,'recognition/teacher_dashboard.html')
			else:
				# Return an 'invalid login' error message.
				return render(request,'recognition/teacher_dashboard.html')
		else:
			messages.warning(request,f'Not a teacher')
			return render(request,'recognition/Four_login.html')
	else:
		form=AuthenticationForm()
	return render(request,'users/loginteachers.html', {'form' : form})



def parentstudentregister(request):
	print("parent-student-register")
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		stdnt_us = User.objects.get(username=username)
		print(stdnt_us,stdnt_us.id)
		dsg = stdnt_us.id
		stdnt_des = desig.objects.get(user_id=dsg)
		print(stdnt_des,stdnt_des.designation)
		stdnt_desig = stdnt_des.designation
		if stdnt_desig == 'parent_student':
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				# Redirect to a success page.
				return render(request,'recognition/parentstudent_dashboard.html')
			else:
				# Return an 'invalid login' error message.
				return render(request,'recognition/parentstudent_dashboard.html')
		else:
			return render(request,'recognition/Four_login.html')
	else:
		form=AuthenticationForm()
	return render(request,'users/login.html', {'form' : form})

@login_required
def add_notification_staff(request):
	# if request.user.username!='admin':
	# 	return redirect('not-authorised')
	print(request.method)
	form = checkForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			Notfi = request.POST.copy()
			notification = Notfi.get('notification')
			print(notification)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Notification Added')
			return render(request,'users/notify.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/notify.html',{'form' : form})

def coursedetails(request):
	print(request.method)
	form = courseForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			course = request.POST.copy()
			cname = course.get('course_name')
			elig = course.get('Eligibility')
			print(cname,elig)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Course Added')
			return render(request,'users/course.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/course.html',{'form' : form})
	
	#return render(request,'recognition/add_notification.html',{'form' : form})

def facultydetails(request):
	print(request.method)
	form = facultyForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			fac = request.POST.copy()
			fname = fac.get('Name')
			qual = fac.get('Qualification')
			print(fname,qual)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Faculty Details Added')
			return render(request,'users/course.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/course.html',{'form' : form})

def add_mark(request):
	print(request.method)
	form = marksForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			mrks = request.POST.copy()
			stdmname = mrks.get('Student_name')
			subj = mrks.get('Subject')
			print(stdmname,subj)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Marks Added')
			return render(request,'users/mrks.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/mrks.html',{'form' : form})
def add_remark(request):
	print(request.method)
	form = remarksForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			remrks = request.POST.copy()
			smname = remrks.get('Student_name')
			rmkz = remrks.get('Subject')
			print(smname,rmkz)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Remarks Added')
			return render(request,'users/mrks.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/mrks.html',{'form' : form})
def view_notification(request):
	print(request.method)
	ntfctn = Notify.objects.all()
	print(ntfctn)
	return render(request,'users/notif.html', {'ntfctn':ntfctn})
	
def add_exam(request):
	print(request.method)
	form = examForm(request.POST)
	if request.method=='POST':
		if form.is_valid:
			exms = request.POST.copy()
			exmname = exms.get('exam_name')
			exmz = exms.get('Subject')
			print(exmname,exmz)
			#form.save(commit=False)
			form.save()
			messages.success(request,'Remarks Added')
			return render(request,'users/atndence.html',{'form' : form})
	else:
		#messages.warning(request,'No notification...')
		return render(request,'users/atndence.html',{'form' : form})

def view_marks(request):
	print(request.method)
	nam=request.user.username
	markz = add_marks.objects.filter(Student_name=nam)
	print(markz)
	return render(request,'users/vw_marks.html', {'markz':markz})


def view_attendance(request):
	nam=request.user.username
	st_us =User.objects.get(username=nam)
	p=st_us.id
	time_qs=Time.objects.filter(user=st_us)
	present_qs=Present.objects.filter(user=st_us)
	date_from=datetime.datetime(2020,1,1)
	date_to=datetime.datetime.now()
	if date_to < date_from:
		messages.warning(request, f'Invalid date selection.')
		return redirect('view-attendance-employee')
	else:
		time_qs=time_qs.filter(date__gte=date_from).filter(date__lte=date_to).order_by('-date')
		present_qs=present_qs.filter(date__gte=date_from).filter(date__lte=date_to).order_by('-date')
		if (len(time_qs)>0 or len(present_qs)>0):
			atd=hours_vs_date_given_employee(present_qs,time_qs,admin=False)
			return render(request,'users/vw_attendance.html',{'atd':atd})
		else:
			messages.warning(request, f'No records for selected duration.')
			return redirect('view-attendance-employee')

def view_remarks(request):
	print(request.method)
	nam=request.user.username
	mkz = add_remarks.objects.filter(Student_name=nam)
	print(mkz)
	return render(request,'users/vw_remarks.html', {'mkz':mkz})


	
