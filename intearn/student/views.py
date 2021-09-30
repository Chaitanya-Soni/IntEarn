from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView ,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import student , Skills ,Education , WorkExperince_Project , Award ,certification
from .forms import SkillForm , EducationForm , WorkExperinceProjectForm , AwardForm ,certificationForm

# Create your views here.
class ProfileManage(LoginRequiredMixin,View):
    template_name = 'student/studentprofile.html'
    def get(self, request,pk=None, *args, **kwargs):
        #formset = SkillsModelFormset(queryset=Skills.objects.none())
        formSkill = SkillForm(request.POST or None, request.FILES or None)
        formEducation = EducationForm(request.POST or None, request.FILES or None)
        formWork = WorkExperinceProjectForm(request.POST or None, request.FILES or None)
        formAward = AwardForm(request.POST or None, request.FILES or None)
        formCert = certificationForm(request.POST or None, request.FILES or None)
        try :
            stu=student.objects.get(user=request.user)
        except student.DoesNotExist:
            stu=None
        context={            
        'student': stu,
        'formskill': formSkill,
        'formEducation': formEducation,
        'formWork': formWork,
        'formAward': formAward,
        'formCert': formCert,
        'Skills': None,
        'work':None,
        'education': None,
        'awards': None,
        'cert': None
        }

        if(pk!=None):
            skill = Skills.objects.get(pk=pk)
            skill.delete()
        #skills
        try:
            skills=Skills.objects.filter(studentpro = student.objects.get(user=self.request.user)) 
            print(skills)
            context['Skills']=skills
        except Skills.DoesNotExist:
            context['Skills']=None
        #education
        try:
            educs=Education.objects.filter(studentpro = student.objects.get(user=self.request.user)) 
            context['education']=educs
        except Education.DoesNotExist:
            context['education']=None
        #work
        try:
            workProjs=WorkExperince_Project.objects.filter(studentpro = student.objects.get(user=self.request.user)) 
            context['work']=workProjs
        except WorkExperince_Project.DoesNotExist:
            context['work']=None
        #Award
        try:
            awards=Award.objects.filter(studentpro = student.objects.get(user=self.request.user)) 
            context['awards']=awards
        except Award.DoesNotExist:
            context['awards']=None
        #Cert
        try:
            certifics=certification.objects.filter(studentpro = student.objects.get(user=self.request.user)) 
            context['cert']=certifics
        except certification.DoesNotExist:
            context['cert']=None
        return render(request, self.template_name, context=context)
    def post(self, request, *args, **kwargs):
        #skill
        form = SkillForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                # only save if name is present
                if form.cleaned_data.get('skill'):
                    skill = form.save(commit=False)
                    skill.studentpro = stu
                    skill.save()
                return redirect('student/profile')
        #education
        form = EducationForm(request.POST)
        if form.is_valid():
                if form.cleaned_data.get('institue') :
                    if form.cleaned_data.get('grade'):
                        if form.cleaned_data.get('startYear'):
                            if form.cleaned_data.get('endYear'):
                                if form.cleaned_data.get('studying'):
                                    educ = form.save(commit=False)
                                    educ.studentpro = stu
                                    educ.save()
                                    return redirect('student/profile')
        #work
        form = SkillForm(request.POST)
        if form.is_valid():
                if form.cleaned_data.get('company') :
                    if form.cleaned_data.get('Position'):
                        if form.cleaned_data.get('description'):
                            if form.cleaned_data.get('startYear'):
                                if form.cleaned_data.get('endYear'):
                                    if form.cleaned_data.get('currently'):
                                        workProj = form.save(commit=False)
                                        workProj.studentpro = stu
                                        workProj.save()
                                        return redirect('student/profile')
        #award
        form = AwardForm(request.POST)
        if form.is_valid():
                if form.cleaned_data.get('nameAward') :
                    if form.cleaned_data.get('Position'):
                        if form.cleaned_data.get('description'):
                            if form.cleaned_data.get('awardYear'):
                                if form.cleaned_data.get('linkAward'):
                                    award = form.save(commit=False)
                                    award.studentpro = stu
                                    award.save()
                                    return redirect('student/profile')
        #cert
        form = certificationForm(request.POST)
        if form.is_valid():
                if form.cleaned_data.get('nameCertificate') :
                    if form.cleaned_data.get('organisation'):
                        if form.cleaned_data.get('certificateYear'):
                            if form.cleaned_data.get('linkCertificate'):
                                certific = form.save(commit=False)
                                certific.studentpro = stu
                                certific.save()
                                return redirect('student/profile')
        return redirect('student/profile')

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
    fields = ['name','phoneno','file']
    success_url = reverse_lazy('student/profile')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)
class ProfileUpadate(LoginRequiredMixin,UpdateView):
    model = student
    fields = ['name','phoneno','file']
    success_url = reverse_lazy('student/profile')

#skills
# $ in js and jquery means get elemnet by id \
class AddSkills(LoginRequiredMixin,View):
    template_name = 'student/Skills_form.html'
    def get(self, request,pk=None, *args, **kwargs):
        #formset = SkillsModelFormset(queryset=Skills.objects.none())
        form = SkillForm(request.POST or None, request.FILES or None)
        if(pk!=None):
            skill = Skills.objects.get(pk=pk)
            skill.delete()
        try:
            skills=Skills.objects.filter(studentpro = student.objects.get(user=self.request.user))
            print(skills)
            return render(request, self.template_name, {'form': form,'skills':skills})
        except Skills.DoesNotExist:
            return render(request, self.template_name, {'form': form,})
    def post(self, request, *args, **kwargs):
        form = SkillForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                # only save if name is present
                if form.cleaned_data.get('skill'):
                    skill = form.save(commit=False)
                    skill.studentpro = stu
                    skill.save()
                return redirect('student/skills')
        return redirect('student/skills')

class AddEducation(LoginRequiredMixin,View):
    template_name = 'student/Education_form.html'
    def get(self, request,pk=None, *args, **kwargs):
        form = EducationForm(request.POST or None, request.FILES or None)
        if(pk!=None):
            educ = Education.objects.get(pk=pk)
            educ.delete()
        try:
            educs=Education.objects.filter(studentpro = student.objects.get(user=self.request.user))
            print(educs)
            return render(request, self.template_name, {'form': form,'educs':educs})
        except Education.DoesNotExist:
            return render(request, self.template_name, {'form': form,})
    def post(self, request, *args, **kwargs):
        form = EducationForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                if form.cleaned_data.get('institue') :
                    if form.cleaned_data.get('grade'):
                        if form.cleaned_data.get('startYear'):
                            if form.cleaned_data.get('endYear'):
                                if form.cleaned_data.get('studying'):
                                    educ = form.save(commit=False)
                                    educ.studentpro = stu
                                    educ.save()
                                    return redirect('student/Education')
        return redirect('student/Education')

class AddWorkExperince_Project(LoginRequiredMixin,View):
    template_name = 'student/WorkProj_form.html'
    def get(self, request,pk=None, *args, **kwargs):
        form = WorkExperinceProjectForm(request.POST or None, request.FILES or None)
        if(pk!=None):
            workProj = WorkExperince_Project.objects.get(pk=pk)
            workProj.delete()
        try:
            workProjs=WorkExperince_Project.objects.filter(studentpro = student.objects.get(user=self.request.user))
            print(workProjs)
            return render(request, self.template_name, {'form': form,'workProjs':workProjs})
        except WorkExperince_Project.DoesNotExist:
            return render(request, self.template_name, {'form': form,})
    def post(self, request, *args, **kwargs):
        form = SkillForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                if form.cleaned_data.get('company') :
                    if form.cleaned_data.get('Position'):
                        if form.cleaned_data.get('description'):
                            if form.cleaned_data.get('startYear'):
                                if form.cleaned_data.get('endYear'):
                                    if form.cleaned_data.get('currently'):
                                        workProj = form.save(commit=False)
                                        workProj.studentpro = stu
                                        workProj.save()
                                        return redirect('student/workProj')
        return redirect('student/workProj')

class AddAward(LoginRequiredMixin,View):
    template_name = 'student/Award_form.html'
    def get(self, request,pk=None, *args, **kwargs):
        form = AwardForm(request.POST or None, request.FILES or None)
        if(pk!=None):
            award = Award.objects.get(pk=pk)
            award.delete()
        try:
            awards=Award.objects.filter(studentpro = student.objects.get(user=self.request.user))
            print(awards)
            return render(request, self.template_name, {'form': form,'awards':awards})
        except Award.DoesNotExist:
            return render(request, self.template_name, {'form': form,})
    def post(self, request, *args, **kwargs):
        form = AwardForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                if form.cleaned_data.get('nameAward') :
                    if form.cleaned_data.get('Position'):
                        if form.cleaned_data.get('description'):
                            if form.cleaned_data.get('awardYear'):
                                if form.cleaned_data.get('linkAward'):
                                    award = form.save(commit=False)
                                    award.studentpro = stu
                                    award.save()
                                    return redirect('student/Award')
        return redirect('student/Award')

class AddCertification(LoginRequiredMixin,View):
    template_name = 'student/Certification_form.html'
    def get(self, request,pk=None, *args, **kwargs):
        form = certificationForm(request.POST or None, request.FILES or None)
        if(pk!=None):
            certific = certification.objects.get(pk=pk)
            certific.delete()
        try:
            certifics=certification.objects.filter(studentpro = student.objects.get(user=self.request.user))
            print(certifics)
            return render(request, self.template_name, {'form': form,'certifics':certifics})
        except certification.DoesNotExist:
            return render(request, self.template_name, {'form': form,})
    def post(self, request, *args, **kwargs):
        form = certificationForm(request.POST)
        stu=student.objects.get(user=self.request.user)
        if form.is_valid():
                if form.cleaned_data.get('nameCertificate') :
                    if form.cleaned_data.get('organisation'):
                        if form.cleaned_data.get('certificateYear'):
                            if form.cleaned_data.get('linkCertificate'):
                                certific = form.save(commit=False)
                                certific.studentpro = stu
                                certific.save()
                                return redirect('student/certification')
        return redirect('student/certification')
