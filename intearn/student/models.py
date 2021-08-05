from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class student(models.Model):
    user=models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    phoneno = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'user'