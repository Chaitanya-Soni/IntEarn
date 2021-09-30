from django.shortcuts import render
from jobpost.models import companyJobPost
from  student.models import student
from  company.models import companyModel
# Create your views here.
def home(request):
    try :
        jobposts=companyJobPost.objects.all()
        context={
        'jobposts': jobposts,
        'student':None,
        'company':None
        }
        if(request.user.is_authenticated==True):
            if(request.user.company==True):
                try : 
                    company=companyModel.objects.get(user=request.user)
                    context['company']=company
                except company.DoesNotExist:
                    context['company']=None

            else:
                try :
                    Student=student.objects.get(user=request.user)
                    context['student']=Student
                except student.DoesNotExist:
                    context['student']=None
        return render(request, "home\index.html",context)
    except companyJobPost.DoesNotExist :
        return render(request, "home\index.html")