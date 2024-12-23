"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import  views

# This is the exercise of personal navigator code
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index, name = 'index'),
#     #path jati pani ghatiya name ko  vhaye pani we can give a beautiful name to grab that path using that name
#     path('about',views.about, name = 'about')
# ]

#adding pipeline
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name= "Home"),
    path('analyze',views.analyze,name= "analyze"),
    path('contactus', views.contactus, name="contactus"),
    path('aboutus', views.aboutus, name="aboutus"),

#     path('capitalizefirst',views.capfirst,name= "capfirst"),
#     path('newlineremove',views.newlineremove,name= "newlineremove"),
#     path('spaceremove',views.spaceremove,name= "spaceremove"),
#     path('charcounter',views.charcounter,name= "charcounter"),

]