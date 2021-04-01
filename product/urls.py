from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.product_add, name='product_add'),
    path('<int:pk>/update_product/', views.product_update, name='product_update'),
    path('<int:pk>/delete_product/', views.product_delete, name='product_delete'),

    # api url
    path('api/rating_avg/<int:pk>/', views.product_rating_avg,
         name='product_rating_avg'),
    path('api/rating_detail/<int:pk>/', views.product_rating_detail,
         name='product_rating_detail'),
    path('api/rating_create/', views.product_rating_create,
         name='product_rating_create'),
    path('api/rating_update/<int:pk>/', views.product_rating_update,
         name='product_rating_update'),
    path('api/rating_delete/<int:pk>/', views.product_rating_delete,
         name='product_rating_delete'),

]
