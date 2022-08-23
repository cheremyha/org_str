""" 
This view for root page to which the user is redirected
after successfully logging in to the site. 
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RootPageView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/root_page.html'
