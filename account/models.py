from django.db import models

# Create your models here.
from  django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=40, unique=True)
    password=models.CharField(max_length=255, blank=True, null= True)
    is_activated=models.BooleanField(default=False)
    activation_code=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.username