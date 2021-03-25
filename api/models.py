from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.




class Schedules(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Schedules are assigned to Emplyees, Employees are auth users
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    note = models.CharField(max_length=100)




