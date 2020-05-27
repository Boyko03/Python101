from django.db import models
from django.utils import timezone


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    lecture_id = models.AutoField(unique=True, primary_key=True)
    lecture_name = models.CharField(max_length=255)
    week = models.IntegerField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    URL = models.URLField()

    def __str__(self):
        return f'Lecture "{self.lecture_name}"'


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Task "{self.name}"'


class Solution(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    date = models.DateTimeField()
    URL = models.URLField()

    def __str__(self):
        return f'Solution for task "{self.task}"'
