from django.db import models
from .models import models

# Create your models here.
class StudentID(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    dateofbirth = models.DateField()
    course = models.CharField(max_length= 100)
    enrollmentdate = models.DateField()