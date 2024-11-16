from django.db import models

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
