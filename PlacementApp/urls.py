"""
URL configuration for PlacementCell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('Companies/', views.Companies, name='Companies'),
    path('stats/', views.stats, name='stats'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('artificialintelligence/', views.artificialintelligence, name='artificialintelligence'),
    path('cloudarchitect/', views.cloudarchitect, name='cloudarchitect'),
    path('contactus/', views.contactus, name='contactus'),
    path('cybersecurityeng/', views.cybersecurityeng, name='cybersecurityeng'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('dashboard3/', views.dashboard3, name='dashboard3'),
    path('dataanalyst/', views.dataanalyst, name='dataanalyst'),
    path('dataarchitect/', views.dataarchitect, name='dataarchitect'),
    path('databaseadmin/', views.databaseadmin, name='databaseadmin'),
    path('datascientist/', views.datascientist, name='datascientist'),
    path('login/', views.login_view, name='login'),
    path('notifs/', views.notifs, name='notifs'),
    path('softwaredev/', views.softwaredev, name='softwaredev'),
    path('informationsecurityanalyst/', views.informationsecurityanalyst, name='informationsecurityanalyst'),
    path('networksecurityadmin/', views.networksecurityadmin, name='networksecurityadmin'),
    path('submit_form_view/', views.submit_form_view, name='submit_form_view'),
    path('logout/', views.logout_user, name='logout'),
    path('job_listings/', views.get_job_listings, name='job_listings'),

]
