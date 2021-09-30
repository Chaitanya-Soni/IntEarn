from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
User = settings.AUTH_USER_MODEL
# Create your models here.
from .validators import validate_file_extension
class student(models.Model):
    user=models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phoneno = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension],blank=True)
    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'user'
class Skills(models.Model):
    studentpro=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    skill=models.CharField( max_length=50)
    def __str__(self):
        return self.skill

    class Meta:
        order_with_respect_to = 'studentpro'
class Education(models.Model):
    studentpro=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    institue = models.CharField( max_length=50)
    grade = models.CharField( max_length=50)
    startYear = models.DateField()
    endYear = models.DateField(null=True)
    studying = models.BooleanField()
    def __str__(self):
        return self.institue

    class Meta:
        order_with_respect_to = 'studentpro'
class WorkExperince_Project(models.Model):
    studentpro=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField( max_length=50)
    Position = models.CharField( max_length=50)
    description = models.TextField()
    startYear = models.DateField()
    endYear = models.DateField(null=True)
    currently = models.BooleanField()
    def __str__(self):
        return self.company

    class Meta:
        order_with_respect_to = 'studentpro'
class Award(models.Model):
    studentpro=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    nameAward = models.CharField( max_length=50)
    Position = models.CharField( max_length=50)
    description = models.TextField()
    awardYear = models.DateField()
    linkAward = models.URLField( max_length=200 , null =True)
    def __str__(self):
        return self.nameAward
    class Meta:
        order_with_respect_to = 'studentpro'
class certification(models.Model):
    studentpro=models.ForeignKey(student ,  on_delete=models.CASCADE, null=True, blank=True)
    nameCertificate = models.CharField( max_length=50)
    organisation = models.CharField( max_length=50)
    certificateYear = models.DateField()
    linkCertificate = models.URLField( max_length=200 , null =True)
    def __str__(self):
        return self.nameCertificate
    class Meta:
        order_with_respect_to = 'studentpro'