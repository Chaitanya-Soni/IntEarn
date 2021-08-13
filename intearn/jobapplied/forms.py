from django.forms import forms, modelformset_factory, ModelForm
from . models import jobApplied 

class JobApplyForm(ModelForm):
    class Meta:
        model = jobApplied
        exclude = ['JobPosted','studentApplied','dateApplied']