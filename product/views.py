from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, ProductUpdateForm


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data['product_title']
            # name = form.cleaned_data['product_name']
            # price = form.cleaned_data['product_price']
            # product = Product(product_title=title,
            #                   product_name=name, product_price=price)
            # product.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'product/product_add.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductUpdateForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product/product_update.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'product/product_delete.html', {"product": product})
