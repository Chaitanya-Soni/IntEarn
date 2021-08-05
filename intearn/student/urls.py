from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', profile ,name='student/profile'),
    path('updateprofile/<int:pk>', ProfileUpadate.as_view() ,name='student/profile/update'),
    path('createprofile/', ProfileCreate.as_view() ,name='student/profile/create'),
]
