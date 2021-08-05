from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import student
# Create your views here.
def profile(request):    
    try:
        stu=student.objects.get(user=request.user)
        context = {
        'student': stu
        }
        return render(request, "student/studentprofile.html",context)
    except student.DoesNotExist:
        return redirect('student/profile/create')
class ProfileDetail(LoginRequiredMixin, DetailView):
    model = student
    context_object_name = 'student'
    template_name = 'student/studentprofile.html'
class ProfileCreate(LoginRequiredMixin,CreateView):
    model = student
    fields = ['name','phoneno']
    success_url = reverse_lazy('student/profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)

class ProfileUpadate(LoginRequiredMixin,UpdateView):
    model = student
    fields = ['name','phoneno']
    success_url = reverse_lazy('student/profile')