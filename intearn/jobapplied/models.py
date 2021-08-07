from django.db import models
from company.models import companyModel
from student.models import student
# Create your models here.

class jobApplied(models.Model):
    companyPosted=models.ForeignKey(companyModel,  on_delete=models.CASCADE, null=True, blank=True)
    studentApplied=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    dateApplied = models.DateTimeField(auto_now=True, auto_now_add=False)
    applied = models.BooleanField()
    def __str__(self):
        return self.companyPosted.companyname+" "+self.studentApplied.name

    class Meta:
        order_with_respect_to = 'dateApplied'