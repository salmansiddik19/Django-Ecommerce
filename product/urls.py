from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.product_add, name='product_add'),
    path('<int:pk>/update_product/', views.product_update, name='product_update'),
    path('<int:pk>/delete_product/', views.product_delete, name='product_delete'),
]
