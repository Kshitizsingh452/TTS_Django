from django.urls import path
from django.views.static import serve
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('get', views.get, name = 'gey'),
    path('reset', views.reset, name = 'reset')
]
