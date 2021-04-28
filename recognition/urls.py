from django.urls import path
from . import views as recog_views


urlpatterns = [
    path('', recog_views.home, name='home'),
    path('Four_login',recog_views.Four_login,name='Four_login'),
    path('dashboard/', recog_views.dashboard, name='dashboard'),
    path('employee_dashboard/',recog_views.employee_dashboard,name='employee_dashboard'),
    path('train/', recog_views.train, name='train'),
    path('add_photos/', recog_views.add_photos, name='add-photos'),
    path('mark_your_attendance', recog_views.mark_your_attendance ,name='mark-your-attendance'),
    path('mark_your_attendance_out', recog_views.mark_your_attendance_out ,name='mark-your-attendance-out'),
    path('view_attendance_home', recog_views.view_attendance_home ,name='view-attendance-home'),
    path('view_attendance_date', recog_views.view_attendance_date ,name='view-attendance-date'),
    path('view_attendance_employee', recog_views.view_attendance_employee ,name='view-attendance-employee'),
    path('not_authorised', recog_views.not_authorised, name='not-authorised'),
    path('add_notification/',recog_views.add_notification,name='add_notification'),
    path('staff_dashboard',recog_views.staff_dashboard,name='staff_dashboard'),
    path('teacher_dashboard',recog_views.teacher_dashboard,name= 'teacher_dashboard'),
    path('parentstudent_dashboard',recog_views.parentstudent_dashboard,name='parentstudent_dashboard')

]
