"""org_str URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from . yasg import urlpatterns as doc_urls
from app.views import (
    EmployeesPaginator,
    EmployeeCreateView,
    EmployeesUpdateView,
    static_tree_page_view,
    dynamic_tree_page_view,
    PositionsViewset,
    EmployeesViewset,
)

router = routers.DefaultRouter()
router.register(r'positions', PositionsViewset)
router.register(r'employees', EmployeesViewset)

urlpatterns = [
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('admin/', admin.site.urls),
    path('static_tree_page', static_tree_page_view),
    path('dynamic_tree_page', dynamic_tree_page_view),
    path('paginate_list', EmployeesPaginator.as_view()),
    path('create/', EmployeeCreateView.as_view()),
    path('update/<int:pk>/', EmployeesUpdateView.as_view(),
         name='employees_update'),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += doc_urls