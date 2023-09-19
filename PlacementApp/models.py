from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField('Name',max_length=100)
    age=models.IntegerField('age')
    def __str__(self) :
        return self.name