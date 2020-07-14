from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from website.forms import UserRegistrationForm
from website.models import User


def error(request, message="Ooops! Aconteceu um erro, vamos investigar, desculpe por esse problema!"):
    # This special view is called everytime there is an error to display it into the browser
    return render(request, 'website/error.html', {'messages': request.messages, })


class IndexView(generic.ListView):
    template_name = 'website/index.html'

    def index(request):
        """"
        Temporary solution while we do not construct the queryset method
        """

        return render(request, 'website/index.html')


class RegisterView:
    def register(request):
        return render(request, 'website/register.html')

    def register_user(request):
        context = {}
        if request.POST:
            if 'user_registration' in request.POST:
                form = UserRegistrationForm(request.POST, request.FILES or None)
                if form.is_valid():
                    incomplete_user = form.save(commit=False)
                    incomplete_user.is_enterprise = False
                    incomplete_user.is_active = False
                    email = form.cleaned_data.get('email')
                    raw_password = form.cleaned_data.get('password1')
                    incomplete_user.save()
                    login(request, incomplete_user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('login')
                else:
                    context['user_registration_form'] = form
        else:
            user_form = UserRegistrationForm()
            context['user_registration_form'] = user_form
        return render(request, 'website/register_user.html', context)


class LoginView(generic.ListView):
    def login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            queryset = User.objects.filter(email=email)
            if len(queryset) != 0:
                if queryset[0].is_active:
                    user = authenticate(email=email, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('index')
                    else:
                        request.messages.append({
                            "type": "warning",
                            "header": "Erro causado pela senha incorreta",
                            "content": "Senha incorreta"
                        })
                        return error(request)
                else:
                    print('inactive')
                    request.messages.append({
                        "type": "warning",
                        "header": "Erro ligado a sua conta",
                        "content": "Sua conta ainda não foi ativada ou foi deletada"
                    })
                    return error(request)

            else:
                request.messages.append({
                    "type": "warning",
                    "header": "Erro ligado ao email",
                    "content": "Email incorreto"
                })
                return error(request)
        else:
            return render(request, 'website/login.html')


class LogoutView(generic.ListView):
    def logout(request):
        logout(request)
        return HttpResponseRedirect('/')


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
