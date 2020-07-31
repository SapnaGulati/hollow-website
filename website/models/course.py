import datetime

from django.db import models


class Course(models.Model):
    title = models.CharField(verbose_name='Título' ,max_length=200)
    macrotopic = models.ManyToManyField('Macrotopic', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Macrotopic(models.Model):
    title = models.CharField(max_length=200)
    microtopic = models.ManyToManyField('Microtopic', on_delete=models.CASCADE)
    exercise_list = models.ForeignKey('ExerciseList', verbose_name='lista de exercícios', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Macrotópico'
        verbose_name_plural = 'Macrotópicos'


class Microtopic(models.Model):
    title = models.CharField(max_length=200)
    video = models.ForeignKey('VideoLesson', on_delete=models.CASCADE)
    importance = models.SmallIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Microtópico'
        verbose_name_plural = 'Microtópicos'


class VideoLesson(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    duration = models.DurationField(default=datetime.timedelta(minutes=0))

    def __str__(self):
        return self.title
         
    class Meta:
        verbose_name = 'Vídeoaula'
        verbose_name_plural = 'Vídeoaulas'
    

class ExerciseList(models.Model):
    title = models.CharField(default='Exercícios e exemplos de aplicação.', max_length=200)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Lista de Exercícios'
        verbose_name_plural = 'Listas de Exercícios'
    
    