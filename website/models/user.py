from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from website.managers import CustomUserManager


def upload_to_name(instance, filename):
    # TODO: Change to 'static/website/profile_pictures/' in production !!!
    return 'website/static/website/profile_pictures/' + filename


class User(AbstractBaseUser):
    """"
    The most important model of our app
    It models the user class

    Interactions with the platform
        - The registration
        - Validation by Admin
        - Add/Change data
        - Personal events (later)
        - Personal development (later)


    Tests that are mandatory
        - The registration was well done
        - Make a check on the registration parameters
        - All required fiels are filled in


    """

    # CHOICES
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro / Não quero declarar')
    )

    # DATABASE FIELDS
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    telephone = PhoneNumberField(blank=True, null=True)
    birthday = models.DateField('Data de nascimento', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.FileField(upload_to=upload_to_name,
                             blank=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    twitter_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    linkedin_link = models.CharField(max_length=200, blank=True, null=True)
    is_subscribed_newsletter = models.BooleanField(default=False)
    address = models.CharField(max_length=500, blank=True, null=True)
    address_complement = models.CharField(max_length=500, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    # Required fields to extend AbstractBaseUser
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # MANAGERS

    # META CLASS
    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    # TO STRING METHOD
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    # SAVE METHOD

    # ABSOLUTE URL METHOD

    # OTHER METHODS
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        Not working for now
        """
        # send_mail(subject, message, from_email, [self.email], **kwargs)
