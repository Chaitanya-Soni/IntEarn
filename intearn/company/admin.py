from django.contrib import admin
from .models import companyModel
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('user', 'companyname', 'phoneno')
admin.site.register(companyModel,MyAdmin)
