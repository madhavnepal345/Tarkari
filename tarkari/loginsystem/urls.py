from django.urls import path
from .views import login_view,register_view,index

urlpatterns = [
    path('',login_view,name='login'),
    path('register/',register_view, name='register'),
    path('home/',index, name='home'),
]
