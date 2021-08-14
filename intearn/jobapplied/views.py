from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import jobApplied
from student.models import student
from jobpost.models import companyJobPost
from .forms import JobApplyForm
class JobApplyList(LoginRequiredMixin, ListView):
    model = jobApplied
    context_object_name = 'jobs'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stu=student.objects.get(user=self.request.user)
        context['jobs'] = context['jobs'].filter(studentApplied=stu)
        context['count'] = context['jobs'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['jobs'] = context['jobs'].filter(JobPosted__contains=search_input)

        return context
class ApplyJob(LoginRequiredMixin,View):
    def get(self, request,pk, *args, **kwargs):
        job=companyJobPost.objects.get(pk=pk)
        stu=student.objects.get(user=self.request.user)
        try:
            try :
                print(0)
                j=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                print(1)
                if(j.apply==True) :
                    return redirect('home')
                else :
                    jobapply=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                    jobapply.apply=True
                    jobapply.save()
                    return redirect('home')
            except jobApplied.DoesNotExist:
                print(11)
                jobapply=jobApplied.objects.create(JobPosted=job,studentApplied=stu,apply=True)
                return redirect('home')
        except companyJobPost.DoesNotExist:
            return redirect('home')
class UnApplyJob(LoginRequiredMixin,View):
    def get(self, request,pk, *args, **kwargs):
        job=companyJobPost.objects.get(pk=pk)
        stu=student.objects.get(user=self.request.user)
        try:
            try :
                j=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                if(j.apply==True) :
                    j.delete()
                return redirect('home')
            except jobApplied.DoesNotExist:
                return redirect('home')
        except companyJobPost.DoesNotExist:
            return redirect('home')
class UnSaveJob(LoginRequiredMixin,View):
    def get(self, request,pk, *args, **kwargs):
        job=companyJobPost.objects.get(pk=pk)
        stu=student.objects.get(user=self.request.user)
        try:
            try :
                j=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                if(j.savePost==True) :
                    j.delete()
                return redirect('home')
            except jobApplied.DoesNotExist:
                return redirect('home')
        except companyJobPost.DoesNotExist:
            return redirect('home')
class SaveJob(LoginRequiredMixin,View):
    def get(self, request,pk, *args, **kwargs):
        job=companyJobPost.objects.get(pk=pk)
        stu=student.objects.get(user=self.request.user)
        try:
            try :
                j=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                if(j.savePost==True) :
                    return redirect('home')
                else :
                    jobapply=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                    jobapply.savePost=True
                    print(jobapply)
                    jobapply.save()
                    return redirect('home')
            except jobApplied.DoesNotExist:
                jobapply=jobApplied(JobPosted=job,studentApplied=stu,savePost=True)
                jobapply.save()
                return redirect('home')
        except companyJobPost.DoesNotExist:
            return redirect('home')