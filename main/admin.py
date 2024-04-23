from django.contrib import admin
from main.models import AppInfo, AboutMe, Sevices, Appointment, MyWorks, Contact

# Register your models here.
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id']
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'date', 'service_type', 'upload_at', 'updated_at']

admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Sevices)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MyWorks)
admin.site.register(Contact)