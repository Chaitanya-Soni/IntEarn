from django.contrib import admin
from .models import student
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phoneno')
admin.site.register(student,MyAdmin)
