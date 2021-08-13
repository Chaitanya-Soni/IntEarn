from django.contrib import admin
from .models import jobApplied
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('JobPosted', 'studentApplied','dateApplied','savePost','apply')
admin.site.register(jobApplied,MyAdmin)
