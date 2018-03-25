from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    work experience = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    about yourself = models.CharField(max_length=30)