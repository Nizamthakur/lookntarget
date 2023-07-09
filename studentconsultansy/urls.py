from django.urls import path
from . import views
urlpatterns = [
    path('', views.s_cun, name = 's_cun'),
]
