# pylint: disable=line-too-long
"""comfucius URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path

from . import views
from . import apis

urlpatterns = [

    path('', views.show_daily_quote_page, name='show_daily_quote_page'), # fallback url
    path('api/', include([
        path('get-fake-quote', apis.get_fake_quote, name='get-fake-quote'),
        path('get-random-fake-quote', apis.get_random_fake_quote, name='get-random-fake-quote'),
        path('generate-new-daily-quote', apis.generate_new_daily_quote, name='generate-new-daily-quote'),
        ])),
    path('show_daily_quote_page', views.show_daily_quote_page, name='show_daily_quote_page'),

]
