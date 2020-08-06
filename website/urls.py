from django.conf.urls import url
from django.urls import path

from website import views

urlpatterns = [
    path('', views.IndexView.index, name='index'),
    path('usuário/', views.UserView.user, name='user_profile'),
    path('usuário/mudar-informações', views.ChangeUserInformationView.edit_profile, name='change_information'),
    path('usuário/mudar-senha', views.ChangePasswordView.changed_password, name='change_password'),
    path('usuário/<int:user_id>', views.UserView.user_profile),
    path('login/', views.LoginView.login, name='login'),
    path('logout/', views.LogoutView.logout, name='logout'),
    path('cadastro/', views.RegisterView.register_user, name='register'),
    path('cadastro/aluno/', views.RegisterView.register_user, name='form_user'),
    path('indique-e-ganhe/', views.ReferAndWinView.as_view, name='referandwin'),
    path('como-funciona', views.HowItWorksView.as_view, name='howitworks'),
    path('quem-somos', views.WhoWeAreView.as_view, name='whoweare'),
    path('contato', views.ContactView.as_view, name='contact'),
    path('trabalhe-conosco', views.WorkWithUsView.as_view, name='workwithus')

]
