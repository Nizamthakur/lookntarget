from django.urls import path
from .views import detailblog
urlpatterns = [
    path ('detailblog/<int:id>/', detailblog)
]
