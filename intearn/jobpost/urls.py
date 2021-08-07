from django.urls import path
from . views import JobList,JobDetail,JobCreate,JobUpdate,JobDelete
urlpatterns = [
    path('joblist/', JobList.as_view() ,name='joblist'),
    path('jobpost/<int:pk>', JobDetail.as_view() ,name='jobpost'),
    path('jobpost-create/', JobCreate.as_view() ,name='jobpost-create'),
    path('jobpost-update/<int:pk>', JobUpdate.as_view() ,name='jobpost-update'),
    path('jobpost-delete/<int:pk>', JobDelete.as_view() ,name='jobpost-delete'),
]