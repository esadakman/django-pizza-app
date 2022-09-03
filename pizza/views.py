from django.shortcuts import render, redirect
from pizza.forms import PizzaForm
from .models import Pizza
from django.contrib import messages

def form_pizza(request):
    form = PizzaForm()
    
    context = {
        'forms': form
    }
    return render(request, 'pizza/home.html', context)


def form(request):
    # global created_pizza_pk 
    created_pizza_pk = 0
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            created_pizza = form.save()
            created_pizza_pk = created_pizza.id
            print(created_pizza_pk)
            messages.success(request, 'Order has .')

            # return redirect("home")
    # context = {
    #     'forms': form,
    #     'pizzaId': created_pizza_pk,
    # }
    # return render(request, 'pizza/order.html', context)
    return render(request, 'pizza/order.html', {'forms': form, 'pizzaId': created_pizza_pk})

def edit(request , id ):
    order = Pizza.objects.get(id=id)
    form = PizzaForm(instance=order)
    if request.method == "POST":
        update_form = PizzaForm(request.POST, instance=order) 
        if update_form.is_valid():
            update_form.save()
            form = update_form
            messages.success(request, 'Order has been updated.')

            return redirect("home")
    context = {
        'forms': form
    }
    return render(request, 'pizza/edit_order.html', context)
