from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('trabalhe-conosco', views.WorkWithUsView.as_view, name='workwithus'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='website/commons/password-reset/password_reset.html',
             subject_template_name='website/commons/password-reset/password_reset_subject.txt',
             email_template_name='website/commons/password-reset/password_reset_email.html',
             success_url='/password-reset/done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='website/commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='website/commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='website/commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
