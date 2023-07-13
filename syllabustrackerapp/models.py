from django.db import models

# Create your models here.
class Course(models.Model):
    Course=models.CharField(max_length=250)
    active=models.BooleanField()
    def __str__(self):
        return self.Course
    
class Day(models.Model):
    Course=models.CharField(max_length=250)
    active=models.BooleanField()
    def __str__(self):
        return self.Day
    
class Syllabus(models.Model):
    Syllabus=models.CharField(max_length=250)
    active=models.BooleanField()
    def __str__(self):
        return self.Syllabus

class Course_syllabus(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Day=models.ForeignKey(Day,on_delete=models.CASCADE)