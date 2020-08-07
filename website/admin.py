from django.contrib import admin

from website.models import Course, Macrotopic, Microtopic, VideoLesson, ExerciseList


class CourseAdmin(admin.ModelAdmin):
    fields = ('macrotopic', 'title')


class MacrotopicAdmin(admin.ModelAdmin):
    fields = ('microtopic', 'exercise_list', 'title')


class MicrotopicAdmin(admin.ModelAdmin):
    fields = ('importance', 'video', 'title')


class VideoLessonAdmin(admin.ModelAdmin):
    fields = ('duration', 'url', 'title')


class ExerciseListAdmin(admin.ModelAdmin):
    fields = ('url', 'title')


admin.site.register(Course, CourseAdmin)
admin.site.register(Macrotopic, MacrotopicAdmin)
admin.site.register(Microtopic, MicrotopicAdmin)
admin.site.register(VideoLesson, VideoLessonAdmin)
admin.site.register(ExerciseList, ExerciseListAdmin)
