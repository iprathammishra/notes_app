from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, re_path, include

from notes import views

app_name = 'notes'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('new', views.new_edit_note, name='create_update'),
    path('<slug:slug>', views.single_note, name='single_note')
]
