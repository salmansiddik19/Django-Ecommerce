from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, ProductUpdateForm
from core.utils import cart_data


def product_detail(request, pk):
    data = cart_data(request)
    cart_item = data['cart_item']
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {'product': product, 'cart_item': cart_item})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data['product_title']
            # name = form.cleaned_data['product_name']
            # price = form.cleaned_data['product_price']
            # image = form.cleaned_data['product_image']
            # product = Product(product_title=title,
            #                   product_name=name, product_price=price, product_image=image)
            # product.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'product/product_add.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductUpdateForm(request.POST or None,
                             request.FILES or None, instance=product)
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
