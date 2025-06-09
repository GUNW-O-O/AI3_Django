from django.urls import path
from . import views

app_name = 'product'
# product 앱의 URL 패턴을 정의합니다.

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_list, name='cart_list'),
    path('cart/add/<int:product_id>/', views.cart_add, name='card_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]