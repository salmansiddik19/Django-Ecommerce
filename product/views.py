from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductRating
from .forms import ProductForm, ProductUpdateForm
from core.utils import cart_data

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .serializers import ProductRatingSerializer


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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_rating_list(request):
    rating = ProductRating.objects.all().order_by('-id')
    serializer = ProductRatingSerializer(rating, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_rating_detail(request, pk):
    rating = ProductRating.objects.get(pk=pk)
    serializer = ProductRatingSerializer(rating, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_rating_create(request):
    serializer = ProductRatingSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        if user != request.user:
            raise PermissionDenied('Wrong user')
        elif ProductRating.objects.filter(product=serializer.validated_data['product']).exists():
            raise PermissionDenied('already done...')
        else:
            serializer.save()
    return Response(serializer.data)
