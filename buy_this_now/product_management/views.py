from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Products

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product saved successfully.")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_list(request):
    products = Products.objects.all().order_by('-id')
    return render(request, 'products/product_list.html', {'products': products})