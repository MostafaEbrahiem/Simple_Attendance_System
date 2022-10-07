from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class attend(models.Model):
    attender = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return str(self.attender.username)+" "+str(self.datetime)[:19]



class Leave(models.Model):
    emp_Leave = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return str(self.emp_Leave.username)+" "+str(self.datetime)[:19]


