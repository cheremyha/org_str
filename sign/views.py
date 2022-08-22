""" Let`s create  Create-generic. """
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    """ View for the registration form. """
    model = User
    form_class = BaseRegisterForm
    success_url = '/'