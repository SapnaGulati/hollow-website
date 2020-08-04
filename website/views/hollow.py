from django.shortcuts import render
from django.views import generic


class ReferAndWinView(generic.ListView):
    def as_view(request):
        return render(request, 'website/referandwin.html')


class HowItWorksView(generic.ListView):
    def as_view(request):
        return render(request, 'website/howitworks.html')


class WhoWeAreView(generic.ListView):
    def as_view(request):
        return render(request, 'website/whoweare.html')


class ContactView(generic.ListView):
    def as_view(request):
        return render(request, 'website/contact.html')


class WorkWithUsView(generic.ListView):
    def as_view(request):
        return render(request, 'website/workwithus.html')
