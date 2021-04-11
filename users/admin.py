from django.contrib import admin
from .models import Present,Time,desig,staff_mesg,Notify
# Register your models here.

admin.site.register(Present)
admin.site.register(Time)
admin.site.register(desig)
admin.site.register(staff_mesg)
admin.site.register(Notify)
