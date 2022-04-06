"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login'),
    path('fivebands/',views.fivebands,name='fivebands'),
    path('start/',views.start,name='start'),
    path('choose/',views.choose,name='choose'),
     path('navbar/',views.navbar,name='navbar'),


    path('alpha/',views.alpha,name='alpha'),
    path('theta/',views.theta,name='theta'),
    path('beta/',views.beta,name='beta'),
    path('delta/',views.delta,name='delta'),


     path('preprocess/',views.preprocess,name='preprocess'),
    path('features/',views.features,name='features'),
    path('classify/<str:jm>/',views.classify,name='classify'),
    path('result/',views.result,name='result'),

     path('delete/',views.delete,name='delete'),

   ]
