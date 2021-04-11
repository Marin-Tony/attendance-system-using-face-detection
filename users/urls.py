from django.urls import path
from . import views  as users_views


urlpatterns = [
    
    path('register/', users_views.register, name='register'),
