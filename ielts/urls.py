from django.urls import path
from . import views
urlpatterns = [
    path('', views.ielts, name = 'ielts'),
]
