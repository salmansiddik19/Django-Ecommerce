from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductRating
from .forms import ProductForm, ProductUpdateForm
from core.utils import cart_data

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .serializers import ProductRatingSerializer
from django.db.models import Count, Avg, Sum, Q
from rest_framework import status


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


# rating information of products
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_rating_avg(request, pk):
    product = get_object_or_404(Product, pk=pk)
    rating_list = product.productrating_set.all().values('user', 'rating')
    average_rating = get_object_or_404(
        Product.objects.annotate(avg_rating=Avg(
            'productrating__rating')).values('id', 'avg_rating'),
        pk=pk
    )
    rating_info = {
        'average_rating': average_rating,
        'list_of_ratings': rating_list,
    }
    return Response(rating_info)


# proudct details page a ai ulr a reqeust kobo, oi sinlge proudct ar avg and list of rating paor jnne, tarpor js dia dui ta value append korbo


# 3 way
#     Head
#     Body
#     Path param


# cata_dic = {
#     'list_of_ratings': total_rating
#     'avg_ratings' 3.6
# }


# aikhane console.log korar kotha chilo, bakita ami dekhay dibo
# ajax(fetch) dia rating add kora dekhabo

# rating's deatil view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_rating_detail(request, pk):
    rating = get_object_or_404(ProductRating, pk=pk)
    serializer = ProductRatingSerializer(rating, many=False)
    return Response(serializer.data)


# rating's create view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_rating_create(request):
    serializer = ProductRatingSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        if ProductRating.objects.filter(Q(product=serializer.validated_data['product']) & Q(user=request.user)).exists():
            raise PermissionDenied('Already done or Wrong user...')
        else:
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data)


# rating's update view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_rating_update(request, pk):
    rating = get_object_or_404(ProductRating, pk=pk)
    print(rating.user)
    if rating.user == request.user:
        serializer = ProductRatingSerializer(
            instance=rating, data=request.data, context={'request': request})
        if serializer.is_valid():
            if rating.product != serializer.validated_data['product']:
                return Response('Wrong product')
            else:
                if rating.update_count < 2:
                    rating.update_count += 1
                    serializer.save()
                    print(serializer.data)
                    return Response(serializer.data)
                else:
                    return Response('You are not allowed to update')
                return Response(serializer.data)
        else:
            return Response('You are not allowed for update...')
    return Response(serializer.data)


# rating's delete view
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def product_rating_delete(request, pk):
    rating = get_object_or_404(ProductRating, pk=pk)
    rating.delete()
    return Response('Delete Successfully...')
