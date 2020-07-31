"""myproject URL Configuration

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
from django.urls import include
from testapp import views as t_views
from exam import views as e_views

urlpatterns = [
    url('testapp/',include('testapp.urls')),
    url('exam/',include('exam.urls')),
    url('Bookapp/',include('Bookapp.urls')),
    #path('test/',e_views.showTest),
    #path('result/',e_views.showResult),
    #path('about/',t_views.about),
    #path('contact/',t_views.showContact),
    #url('^$',t_views.greeting),
    path('admin/', admin.site.urls),
]
