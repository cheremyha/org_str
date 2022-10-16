"""
Import this module to integrate your python script with the django project.
"""
import os
from django.core.wsgi import get_wsgi_application


def create_con():
    """
    Set connection between local script and django project.
    :return:None
    """
    os.environ['DJANGO_SETTINGS_MODULE'] = 'org_str.org_str.settings'
    application = get_wsgi_application()


create_con()


if __name__ == '__main__':
    create_con()
    print('The test finished successfully')