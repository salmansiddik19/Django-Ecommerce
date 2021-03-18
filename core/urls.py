from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/users/', views.user_list, name='user_list'),
    path('dashboard/users/<int:pk>/', views.user_detail, name='user_detail'),
    path('dashboard/users/signup', views.user_signup, name='user_signup'),
    path('dashboard/products/', views.product_list, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('signuup/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signup/comfirm/', views.signup_confirm, name='signup_confirm'),
    path('signup/complete/', views.signup_complete, name='signup_complete'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
]
