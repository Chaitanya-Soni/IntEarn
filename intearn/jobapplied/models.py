from django.db import models
from company.models import companyModel
from student.models import student
from jobpost.models import companyJobPost
# Create your models here.

class jobApplied(models.Model):
    JobPosted=models.ForeignKey(companyJobPost,  on_delete=models.CASCADE, null=True, blank=True)
    studentApplied=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    dateApplied = models.DateTimeField(auto_now=True, auto_now_add=False)
    savePost = models.BooleanField(default=False , null=True )
    apply = models.BooleanField(default=False , null=True )
    def __str__(self):
        return str(self.JobPosted)+" "+str(self.studentApplied)

    class Meta:
        order_with_respect_to = 'dateApplied'
