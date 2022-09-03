from django.urls import path
from .views import form, form_pizza
# from 

urlpatterns = [
    path('', form_pizza, name='home'),
    path('order/', form, name='home'),
     
]