from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('',include('home.urls')),
    path('student/',include('student.urls')),
    path('company/',include('company.urls')),
    path('companyJobs/',include('jobpost.urls')),
    path('jobapplied/',include('jobapplied.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)