from django.db import models

class teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    office_details = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()


class course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    classroom = models.CharField(max_length=30)
    times = models.TimeField()
    teacher = models.ForeignKey(teacher, blank=True)
    students = models.ManyToManyField('student', blank=True)


class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    courses = models.ManyToManyField('course', through=course.students.through, blank=True)
