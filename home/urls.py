from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Welcome to Fun Coding wth Rahul"
admin.site.site_title = "Rahul's title"
admin.site.index_header = "Rahul's index"

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
