from django.contrib import admin
from .models import student,Skills,Education,WorkExperince_Project,Award,certification
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phoneno','file')
admin.site.register(student,MyAdmin)

class MyAdminSkills(admin.ModelAdmin):
    list_display = ('skill', 'studentpro')
admin.site.register(Skills,MyAdminSkills)

class MyAdminEducation(admin.ModelAdmin):
    list_display = ('studentpro','institue','grade','startYear','endYear', 'studying')
admin.site.register(Education,MyAdminEducation)

class MyAdminWorkExperince_Project(admin.ModelAdmin):
    list_display = ('studentpro','company','Position','description','startYear','endYear','currently')
admin.site.register(WorkExperince_Project,MyAdminWorkExperince_Project)

class MyAdminAward(admin.ModelAdmin):
    list_display = ('studentpro','nameAward','Position','description','awardYear','linkAward')
admin.site.register(Award,MyAdminAward)

class MyAdmincertification(admin.ModelAdmin):
    list_display = ('studentpro','nameCertificate','organisation','certificateYear','linkCertificate')
admin.site.register(certification,MyAdmincertification)