from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import companyModel
# Create your views here.
def profile(request):    
    try:
        comp=companyModel.objects.get(user=request.user)
        context = {
        'company': comp
        }
        return render(request, "company/companyprofile.html",context)
    except companyModel.DoesNotExist:
        return redirect('company/profile/create')
class ProfileDetail(LoginRequiredMixin, DetailView):
    model = companyModel
    context_object_name = 'companyModel'
    template_name = 'company/companyprofile.html'
class ProfileCreate(LoginRequiredMixin,CreateView):
    model = companyModel
    fields = ['companyname','phoneno']
    success_url = reverse_lazy('company/profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)

class ProfileUpadate(LoginRequiredMixin,UpdateView):
    model = companyModel
    fields = ['companyname','phoneno']
    success_url = reverse_lazy('company/profile')