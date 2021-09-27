from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', ProfileManage.as_view() ,name='student/profile'),
    path('updateprofile/<int:pk>', ProfileUpadate.as_view() ,name='student/profile/update'),
    path('createprofile/', ProfileCreate.as_view() ,name='student/profile/create'),
    path('skills/', AddSkills.as_view() ,name='student/skills'),
    path('skills/<int:pk>', AddSkills.as_view() ,name='student/deleteskill'),
    path('Education/', AddEducation.as_view() ,name='student/Education'),
    path('Education/<int:pk>', AddEducation.as_view() ,name='student/deleteEducation'),
    path('workProj/', AddWorkExperince_Project.as_view() ,name='student/workProj'),
    path('workProj/<int:pk>', AddWorkExperince_Project.as_view() ,name='student/deleteworkProj'),
    path('Award/', AddAward.as_view() ,name='student/Award'),
    path('Award/<int:pk>', AddAward.as_view() ,name='student/deleteAward'),
    path('certification/', AddCertification.as_view() ,name='student/certification'),
    path('certification/<int:pk>', AddCertification.as_view() ,name='student/deletecertification'),


]
