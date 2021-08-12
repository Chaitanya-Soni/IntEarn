from django.shortcuts import render,redirect
from .models import companyJobPost
from company.models import companyModel
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class JobDetail( DetailView):
    model = companyJobPost
    context_object_name = 'companyJobPost'
    template_name = 'jobpost/companyJobPost.html'
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