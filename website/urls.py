from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('login/', views.LoginView.login, name='login'),
    path('logout/', views.LogoutView.logout, name='logout'),
    path('register/', views.RegisterView.register, name='register'),
    path('indiqueeganhe/', views.ReferAndWinView.as_view, name='referandwin'),
    path('comofunciona', views.HowItWorksView.as_view, name='howitworks'),
    path('quemsomos', views.WhoWeAreView.as_view, name='whoweare'),
    path('contato', views.ContactView.as_view, name='contact')

]
