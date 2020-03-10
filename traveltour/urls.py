"""traveltour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from lodgingevents import views as lodge_views
from travelevents import views as travel_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/lodgingevents/$', lodge_views.event_list),
    url(r'^api/lodgingevents/(?P<event_pk>[0-9]+)$', lodge_views.event_detail),
    url(r'^api/travelevents/$', travel_views.event_list),
    url(r'^api/travelevents/(?P<event_pk>[0-9]+)$', travel_views.event_detail),
]
