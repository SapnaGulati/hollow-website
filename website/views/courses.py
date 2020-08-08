from django.shortcuts import render
from django.views import generic

from website.models import Course


class CoursesView(generic.ListView):
    def as_view(request, course_id):
        course = Course.objects.get(id=course_id)
        context = {
            "course": course
        }
        return render(request, 'website/course_page.html', context)

    def courses_view(request):

        courses = Course.objects.all()

        return render(request, 'website/courses.html', {'courses': courses})
