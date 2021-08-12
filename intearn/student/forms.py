from django.forms import forms, modelformset_factory, ModelForm
from .models import Skills,Education,WorkExperince_Project,Award,certification

class SkillForm(ModelForm):
    class Meta:
        model = Skills
        exclude = ['studentpro']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['studentpro']

class WorkExperinceProjectForm(ModelForm):
    class Meta:
        model = WorkExperince_Project
        exclude = ['studentpro']

class AwardForm(ModelForm):
    class Meta:
        model = Award
        exclude = ['studentpro']

class certificationForm(ModelForm):
    class Meta:
        model = certification
        exclude = ['studentpro']


