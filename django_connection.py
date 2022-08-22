"""
Import this module to integrate your python script with the django project.
"""
from django.core.wsgi import get_wsgi_application
import os


def create_con():
    """
    Set connection between local script and django project.
    :return:None
    """
    os.environ['DJANGO_SETTINGS_MODULE'] = 'org_str.settings'
    application = get_wsgi_application()


create_con()


