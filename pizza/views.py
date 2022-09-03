from django.shortcuts import render
from pizza.forms import PizzaForm



def form_pizza(request):
    form = PizzaForm()

    context = {
        'forms': form
    }
    return render(request, 'pizza/order.html', context)
