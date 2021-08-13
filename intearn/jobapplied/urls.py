from django.urls import path
from .views import *
urlpatterns = [
    path('apply/<int:pk>', ApplyJob.as_view() ,name='jobApply/student'),
    path('save/<int:pk>', SaveJob.as_view() ,name='jobSave/student'),
    path('unsave/<int:pk>', UnSaveJob.as_view() ,name='jobUnSave/student'),
    path('unapply/<int:pk>', UnApplyJob.as_view() ,name='jobUnApply/student'),
    path('joblist/', JobApplyList.as_view() ,name='jobApplylist'),
]
