from django.shortcuts import render,redirect
from .models import companyJobPost
from company.models import companyModel
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from student.models import student
from jobapplied.models import jobApplied
# Create your views here.
class JobList(LoginRequiredMixin, ListView):
    model = companyJobPost
    context_object_name = 'companyJobPost'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company=companyModel.objects.get(user=self.request.user)
        context['companyJobPost'] = context['companyJobPost'].filter(companyPosted=company)
        context['count'] = context['companyJobPost'].count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['companyJobPost'] = context['companyJobPost'].filter(jobdescrption__contains=search_input)

        return context
class ApplyJobList(LoginRequiredMixin, ListView):
    template_name = 'jobpost/applicants.html'
    context_object_name = 'applicants'
    def get_queryset(self):
        comp = companyJobPost.objects.get(pk=self.kwargs['pk'],accepting=True)
        job = jobApplied.objects.filter(JobPosted=comp)    
        return job
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job=companyJobPost.objects.get(pk=self.kwargs['pk'])
        context['jobname'] = job
        return context

class JobDetail( DetailView):
    model = companyJobPost
    context_object_name = 'companyJobPost'
    template_name = 'jobpost/companyJobPost.html'
    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        try :
            job=companyJobPost.objects.get(pk=self.object.pk)
            stu=student.objects.get(user=self.request.user)
            try :
                    j=jobApplied.objects.get(JobPosted=job,studentApplied=stu)
                    if(j.apply==True):
                        context['apply']=False
                    else :
                        context['apply']=True
                    if(j.savePost==True):
                        context['save']=False
                    else :
                        context['save']=True
                    context['job']=job
                    return context
            except jobApplied.DoesNotExist:
                    context['save']=True
                    context['apply']=True
                    context['job']=job
                    return context
        except student.DoesNotExist:
            context['save']=False
            context['apply']=False
            context['job']=job
            return context    
        
class JobCreate(LoginRequiredMixin,CreateView):
    model = companyJobPost
    fields = ['jobname','jobdescrption','jobStipend','accepting']
    success_url = reverse_lazy('joblist')
    def form_valid(self, form):
        form.instance.companyPosted = companyModel.objects.get(user=self.request.user)
        print(form.instance.companyPosted)
        return super(JobCreate, self).form_valid(form)

class JobUpdate(LoginRequiredMixin,UpdateView):
    model = companyJobPost
    fields = ['jobname','jobdescrption','jobStipend','accepting']
    success_url = reverse_lazy('joblist')
class JobDelete(LoginRequiredMixin,DeleteView):
    model = companyJobPost
    context_object_name = 'companyJobPost'
    success_url = reverse_lazy('joblist') 