from django.urls import path
from . import views
urlpatterns = [
    path('rayan', views.index, name='index'),
    path('add_task', views.add, name='add'),
]

