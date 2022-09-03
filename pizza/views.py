from django.shortcuts import render, redirect
from pizza.forms import PizzaForm
from .models import Pizza


def form_pizza(request):
    form = PizzaForm()
    
    context = {
        'forms': form
    }
    return render(request, 'pizza/home.html', context)


def form(request):
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,"Todo created successfully")
            return redirect("home")
    context = {
        'forms': form
    }
    return render(request, 'pizza/order.html', context)

def edit(request , id ):
    order = Pizza.objects.get(id=id)
    form = PizzaForm(instance=order)
    if request.method == "POST":
        update_form = PizzaForm(request.POST, instance=order) 
        if update_form.is_valid():
            update_form.save()
            form = update_form
            # messages.success(request,"Todo created successfully")
            return redirect("home")
    context = {
        'forms': form
    }
    return render(request, 'pizza/edit_order.html', context)
