from django.db import models
from django.conf import settings
# Create your models here.
class student(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, null=True, blank=True)
    studentname = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'