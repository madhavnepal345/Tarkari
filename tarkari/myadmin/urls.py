from django.urls import path
from . views  import dashboard

urlpatterns = [
    path('admi/', dashboard, name='admin'),
]
