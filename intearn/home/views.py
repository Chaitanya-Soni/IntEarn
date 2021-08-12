from django.shortcuts import render
from jobpost.models import companyJobPost
# Create your views here.
def home(request):
    try :
        jobposts=companyJobPost.objects.all()
        context={
        'jobposts': jobposts
        }
        return render(request, "home\index.html",context)
    except companyJobPost.DoesNotExist :
        return render(request, "home\index.html")