from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signuup/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signup/comfirm/', views.signup_confirm, name='signup_confirm'),
    path('signup/complete/', views.signup_complete, name='signup_complete'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
]
