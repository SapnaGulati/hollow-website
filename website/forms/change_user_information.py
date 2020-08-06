from django import forms
from django.forms import DateInput
from phonenumber_field.formfields import PhoneNumberField

from website.models import User


class EditProfileForm(forms.ModelForm):
    telephone = PhoneNumberField(label="Número de telefone : ", required=False)
    twitter_link = forms.CharField(label='Link twitter : ', required=False)
    linkedin_link = forms.CharField(label='Link LinkedIn : ', required=False)
    first_name = forms.CharField(label='Primeiro nome : ', required=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'telephone',
            'gender',
            'photo',
            'birthday',
            'job_title',
            'twitter_link',
            'linkedin_link',
            'is_subscribed_newsletter',
            'address',
            'address_complement',
            'zip_code',
            'city',
            'country'
        )
        labels = {
            'last_name': 'Nome de família : ',
            'birthday': 'Data de nascimento : ',
            'job_title': 'Profissão : ',
            'gender': 'Sexo : ',
            'photo': 'Foto de perfil',
            'is_subscribed_newsletter': 'Gostaria de me inscrever na newsletter',
            'address': 'Endereço : ',
            'address_complement': 'Complemento do endereço : ',
            'zip_code': 'Código postal : ',
            'city': 'Cidade : ',
        }
        widgets = {
            'birthday': DateInput(),
        }
