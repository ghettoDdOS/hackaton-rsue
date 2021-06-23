"""hackaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from team_managment import views as team_managment_views

admin.site.site_header = "RINH HACK Admin"
admin.site.site_title = "RINH HACK Admin"
admin.site.index_title = "RINH HACK Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", team_managment_views.index),
    path("registration", team_managment_views.register),
    path("registration-team", team_managment_views.register_team),
]
