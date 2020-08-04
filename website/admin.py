from django.contrib import admin

from website.models import Course, Macrotopic, Microtopic, VideoLesson, ExerciseList

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    fields = ('macrotopic', 'title')
    pass


class MacrotopicAdmin(admin.ModelAdmin):
    fields = ('microtopic', 'exercise_list', 'title')
    pass


class MicrotopicAdmin(admin.ModelAdmin):
    fields = ('importance' ,'video', 'title')
    pass


class VideoLessonAdmin(admin.ModelAdmin):
    fields = ('duration', 'url', 'title')
    pass


class ExerciseListAdmin(admin.ModelAdmin):
    fields = ('url', 'title')
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Macrotopic, MacrotopicAdmin)
admin.site.register(Microtopic, MicrotopicAdmin)
admin.site.register(VideoLesson, VideoLessonAdmin)
admin.site.register(ExerciseList, ExerciseListAdmin)