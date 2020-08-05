from django.shortcuts import render
from django.views import generic

from website.models import User


class UserView(generic.ListView):
    template_name = 'website/user_profile.html'

    def user(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        return render(request, 'website/user_profile.html')

    def user_profile(request, user_id):
        """"
        Temporary solution while we do not construct the queryset method
        """

        try:
            user = User.objects.get(id=user_id)
            return render(request, 'website/user_profile.html', {'user': user})
        except User.DoesNotExist:
            return render(request, 'website/user_does_not_exist.html')


class ChangeInformationView(generic.ListView):
    template_name = 'website/change_information.html'

    def change_information(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        return render(request, 'website/change_information.html')


class ChangePasswordView(generic.ListView):
    template_name = 'website/change_password.html'

    def changed_password(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        return render(request, 'website/change_password.html')
