import datetime

from django.db import models


class Course(models.Model):
    # DATABASE FIELDS
    title = models.CharField(verbose_name='Título' ,max_length=200)
    macrotopic = models.ManyToManyField('Macrotopic', verbose_name='Macrotópico')
    
    # META CLASS
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    # TO STRING METHOD
    def __str__(self):
        return self.title


class Macrotopic(models.Model):
    # DATABASE FIELDS
    title = models.CharField(verbose_name='Título', max_length=200)
    microtopic = models.ManyToManyField('Microtopic', verbose_name='Microtópico')
    exercise_list = models.ForeignKey('ExerciseList', verbose_name='Lista de Exercícios', on_delete=models.CASCADE)
    
    # META CLASS
    class Meta:
        verbose_name = 'Macrotópico'
        verbose_name_plural = 'Macrotópicos'

    # TO STRING METHOD
    def __str__(self):
        return self.title


class Microtopic(models.Model):
    # DATABASE FIELDS
    title = models.CharField(verbose_name='Título', max_length=200)
    video = models.ForeignKey('VideoLesson', verbose_name='Vídeoaula', on_delete=models.CASCADE)
    importance = models.SmallIntegerField(verbose_name='Importância')


    # META CLASS
    class Meta:
        verbose_name = 'Microtópico'
        verbose_name_plural = 'Microtópicos'

    # TO STRING METHOD
    def __str__(self):
        return self.title
    

class VideoLesson(models.Model):
    # DATABASE FIELDS
    title = models.CharField(verbose_name='Título', max_length=200)
    url = models.URLField(max_length=200)
    duration = models.DurationField(verbose_name='Duração', default=datetime.timedelta(minutes=0))


    # META CLASS
    class Meta:
        verbose_name = 'Vídeoaula'
        verbose_name_plural = 'Vídeoaulas'

    # TO STRING METHOD
    def __str__(self):
        return self.title    


class ExerciseList(models.Model):
    # DATABASE FIELDS
    title = models.CharField(verbose_name='Título', default='Exercícios e exemplos de aplicação.', max_length=200)
    url = models.URLField(max_length=200)
    
    # META CLASS
    class Meta:
        verbose_name = 'Lista de Exercícios'
        verbose_name_plural = 'Listas de Exercícios'
    
    # TO STRING METHOD
    def __str__(self):
        return self.title
    
    