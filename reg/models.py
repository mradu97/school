from django.db import models

# Create your models here.
class Student(models.Model):
    s_nm=models.CharField(max_length=30)
    sclass=models.CharField(max_length=10)
    sdob=models.DateTimeField('')

    def __str__(self):
        return self.s_nm
        