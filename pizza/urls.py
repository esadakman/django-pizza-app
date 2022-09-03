from django.urls import path
from .views import form_pizza
# from 

urlpatterns = [
    path('order', form_pizza, name='home'),
     
]