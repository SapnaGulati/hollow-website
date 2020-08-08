from django.shortcuts import render
from django.views import generic


class CoursesView(generic.ListView):
    def as_view(request):
        return render(request, 'website/course_page.html')
