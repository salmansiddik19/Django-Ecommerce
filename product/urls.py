from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.product_add, name='product_add'),
    path('<int:pk>/update_product/', views.product_update, name='product_update'),
    path('<int:pk>/delete_product/', views.product_delete, name='product_delete'),

    # api url
    path('api/rating_list/', views.product_rating_list,
         name='product_rating_list'),
    path('api/rating_detail/<int:pk>/', views.product_rating_detail,
         name='product_rating_detail'),
    path('api/rating_create/', views.product_rating_create,
         name='product_rating_create'),

]
