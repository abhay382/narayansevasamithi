from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path("about/", views.about, name="about"),
     path("contact/", views.contact, name="about"),
     path("gallery/", views.gallery, name="about"),
     path("event/", views.event, name="about"),
     path("donate/", views.donate, name="about"),
     path("vol/", views.vol, name="about"),
     path("camp/", views.camp, name="about"),
     path("vol/", views.vol, name="about"),
     path("fund/", views.fund, name="about"),
     path("joinnow/", views.joinnow, name="about"),
path("phil/", views.phil, name="about")

]

