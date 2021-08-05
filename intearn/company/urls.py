from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', profile ,name='company/profile'),
    path('updateprofile/<int:pk>', ProfileUpadate.as_view() ,name='company/profile/update'),
    path('createprofile/', ProfileCreate.as_view() ,name='company/profile/create'),
]
