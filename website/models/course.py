from django.db import models


class Course(models.Model):
    title = models.CharField()
    macrotopic = models.ForeignKey(Macrotopic, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Macrotopic(models.Model):
    title = models.CharField()
    microtopic = models.ForeignKey(microtopic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Microtopic(models.Model):
    title = models.CharField()
    video = models.ForeignKey(VideoLesson, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class VideoLesson(models.Model):
    title = models.CharField()
    def __str__(self):
        return self.title
         