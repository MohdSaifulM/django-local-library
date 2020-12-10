from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Library(models.Model):
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.branch
    

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=50, null=True)
    date_borrowed = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="books", blank=True)
    branch = models.ForeignKey(Library, null=True, on_delete=models.CASCADE, related_name="books")
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
