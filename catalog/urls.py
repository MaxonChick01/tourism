from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('tours', tours, name='tours'),
    path('tours/<slug:slug>', tours_specify, name='tours_specify'),
    path('<int:pk>', single_tour, name='single_tour')
]