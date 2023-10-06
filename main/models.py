from django.db import models
from django.utils import timezone
from  account.models import Account
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    company_name = models.CharField(max_length=200)
    decription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(Account, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts')
    location=models.CharField(max_length=100)
    deadline=models.DateTimeField()
    vacancy=models.TextField(blank=True, null=True)
    attributes=models.TextField(blank=True, null=True)
    price_range=models.CharField(max_length=10, blank=True, null=True)
    expired = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        # Check if the post's deadline has passed
        if self.deadline < timezone.now():
            self.expired = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name
