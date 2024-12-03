from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length=20)
    admNo = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    image = models.ImageField(upload_to='student_images/', blank=True)

    # Constructor to return one of the values
    def __str__(self):
        return self.name