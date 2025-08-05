from django.urls import path
from recipes.views import about, home, contact



urlpatterns = [
    path('about/',about),
    path('contact/',contact),
    path('',home),
]