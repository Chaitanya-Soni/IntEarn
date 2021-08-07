from django.contrib import admin
from django.urls import path ,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('',include('home.urls')),
    path('student/',include('student.urls')),
    path('company/',include('company.urls')),
    path('companyJobs/',include('jobpost.urls')),
]