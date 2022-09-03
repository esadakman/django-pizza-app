from django.urls import path
from .views import edit, form, form_pizza
# from 

urlpatterns = [
    path('', form_pizza, name='home'),
    path('order/', form, name='order'),
    path('edit/<int:id>', edit, name='edit'),
     
]