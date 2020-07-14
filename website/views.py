from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'website/index.html'

    def index(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        return render(request, 'website/index.html')