from django.urls import path
from . import views

app_name = 'upload_file'

urlpatterns = [
    path('', views.index, name='index')
]