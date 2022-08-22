from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RootPageView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/root_page.html'