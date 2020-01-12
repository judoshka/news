from django.urls import path, include
from website.views import home_render

urlpatterns = [
    path('', home_render, name='home'),
]