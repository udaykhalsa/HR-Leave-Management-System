from django.contrib import admin
from .models import LeaveApplication, LeaveList

class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('reason', 'from_date', 'to_date')

class LeaveListAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_date', 'to_date', 'leave_status')


admin.site.register(LeaveApplication, LeaveApplicationAdmin)
admin.site.register(LeaveList, LeaveListAdmin)
