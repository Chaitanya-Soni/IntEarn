from django.db import models
from company.models import companyModel
from student.models import student
from jobpost.models import companyJobPost
# Create your models here.

class jobApplied(models.Model):
    JobPosted=models.ForeignKey(companyJobPost,  on_delete=models.CASCADE, null=True, blank=True)
    studentApplied=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    dateApplied = models.DateTimeField(auto_now=True, auto_now_add=False)
    saved = models.BooleanField()
    applied = models.BooleanField()
    linkdien =models.URLField( max_length=200,null=True)
    github =models.URLField( max_length=200,null=True)
    def __str__(self):
        return self.companyPosted.companyname+" "+self.studentApplied.name

    class Meta:
        order_with_respect_to = 'dateApplied'
class Skills(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    skill=models.CharField( max_length=50)
    def __str__(self):
        return self.skill

    class Meta:
        order_with_respect_to = 'jobapplied'
class Education(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    institue = models.CharField( max_length=50)
    grade = models.CharField( max_length=50)
    startYear = models.DateField()
    endYear = models.DateField(null=True)
    studying = models.BooleanField()
    def __str__(self):
        return self.institue

    class Meta:
        order_with_respect_to = 'jobapplied'
class WorkExperince_Project(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    company = models.CharField( max_length=50)
    Position = models.CharField( max_length=50)
    description = models.TextField()
    startYear = models.DateField()
    endYear = models.DateField(null=True)
    currently = models.BooleanField()
    def __str__(self):
        return self.company

    class Meta:
        order_with_respect_to = 'jobapplied'
class Award(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    nameAward = models.CharField( max_length=50)
    Position = models.CharField( max_length=50)
    description = models.TextField()
    awardYear = models.DateField()
    linkAward = models.URLField( max_length=200 , null =True)
    def __str__(self):
        return self.nameAward
    class Meta:
        order_with_respect_to = 'jobapplied'
class certification(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    nameCertificate = models.CharField( max_length=50)
    organisation = models.CharField( max_length=50)
    certificateYear = models.DateField()
    linkCertificate = models.URLField( max_length=200 , null =True)
    def __str__(self):
        return self.nameCertificate
    class Meta:
        order_with_respect_to = 'jobapplied'

class Skills(models.Model):
    jobapplied = models.ForeignKey(jobApplied, on_delete=models.CASCADE ,null =True ,blank =True)
    skill=models.CharField( max_length=50)
    def __str__(self):
        return self.skill

    class Meta:
        order_with_respect_to = 'jobapplied'