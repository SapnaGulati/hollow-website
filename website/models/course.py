import datetime

from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    macrotopic = models.ForeignKey('Macrotopic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Macrotopic(models.Model):
    title = models.CharField(max_length=200)
    microtopic = models.ForeignKey('Microtopic', on_delete=models.CASCADE)
    exercise_list = models.ForeignKey('ExerciseList', verbose_name='exercise list', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Microtopic(models.Model):
    title = models.CharField(max_length=200)
    video = models.ForeignKey('VideoLesson', on_delete=models.CASCADE)
    importance = models.SmallIntegerField()

    def __str__(self):
        return self.title


class VideoLesson(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    duration = models.DurationField(default=datetime.timedelta(minutes=0))

    def __str__(self):
        return self.title
         

class ExerciseList(models.Model):
    title = models.CharField(default='Exercícios e exemplos de aplicação.', max_length=200)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    