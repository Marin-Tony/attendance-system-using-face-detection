from django.urls import path
from . import views  as users_views

urlpatterns = [
    
    path('register/', users_views.register, name='register'),
    path('staff_register/',users_views.staff_register,name='staff_register'),
    path('teacheregister/',users_views.teacheregister,name='teacheregister'),
    path('parentstudentregister/',users_views.parentstudentregister,name='parentstudentregister'),
    path('add_notification_staff',users_views.add_notification_staff,name='add_notification_staff'),
    path('coursedetails',users_views.coursedetails,name='coursedetails'),
    path('facultydetails',users_views.facultydetails,name='facultydetails'),
    path('add_mark',users_views.add_mark,name='add_mark'),
    path('add_remark',users_views.add_remark,name='add_remark'),
    path('view_notification',users_views.view_notification,name='view_notification'),
    path('view_marks',users_views.view_marks,name='view_marks'),
    path('view_attendance',users_views.view_attendance,name='view_attendance'),
    path('view_remarks',users_views.view_remarks,name='view_remarks'),

    
   #https:128.0.0.1/users/register/

]
