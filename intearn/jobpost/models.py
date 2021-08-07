from django.db import models
from company.models import companyModel
# Create your models here.
class companyJobPost(models.Model):
    companyPosted=models.ForeignKey(companyModel,  on_delete=models.CASCADE, null=True, blank=True)
    jobname = models.CharField(max_length=200)
    jobdescrption = models.TextField(null=True, blank=True)
    jobStipend = models.TextField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    accepting = models.BooleanField()
    def __str__(self):
        return self.companyPosted.companyname

    class Meta:
        order_with_respect_to = 'dateCreated'