from django.urls import path
from . import views as recog_views


urlpatterns = [
    path('', recog_views.home, name='home'),
    path('dashboard/', recog_views.dashboard, name='dashboard'),
    path('train/', recog_views.train, name='train'),
    path('add_photos/', recog_views.add_photos, name='add-photos'),
    path('mark_your_attendance', recog_views.mark_your_attendance ,name='mark-your-attendance'),
    path('mark_your_attendance_out', recog_views.mark_your_attendance_out ,name='mark-your-attendance-out'),
    path('view_attendance_home', recog_views.view_attendance_home ,name='view-attendance-home'),
    path('view_attendance_date', recog_views.view_attendance_date ,name='view-attendance-date'),
    path('view_attendance_employee', recog_views.view_attendance_employee ,name='view-attendance-employee'),
    path('view_my_attendance', recog_views.view_my_attendance_employee_login ,name='view-my-attendance-employee-login'),
    path('not_authorised', recog_views.not_authorised, name='not-authorised'),
    path('add_notification',recog_views.add_notification,name='add_notification'),
    #path('add_events',recog_views.add_events,name='add_events'),
    path('mesg_staff',recog_views.mesg_staff,name='mesg_staff'),

]
