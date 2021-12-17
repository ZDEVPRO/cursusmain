from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),

    path('orders_product/', views.user_orders_product, name='user_orders_product'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),

    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),

]