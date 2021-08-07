from django.contrib import admin
from .models import companyJobPost
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('companyPosted', 'jobname','jobStipend','dateCreated','accepting')
admin.site.register(companyJobPost,MyAdmin)
