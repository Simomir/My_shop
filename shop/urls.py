from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.landing, name='landing page'),
    path('create/', views.create_product, name='create product'),
    path('detail/<int:pk>/', views.ProductDetail.as_view(), name='product detail'),
    path('edit/<int:pk>/', views.UpdateProductView.as_view(), name='edit product'),
    path('delete/<int:pk>/', views.delete, name='delete product'),
    path('all/', views.ShopIndex.as_view(), name='shop index'),
    path('owned/', views.UserOwnedProducts.as_view(), name='own products'),
    path('owned/detail/<int:pk>/', views.UserOwnProductDetail.as_view(), name='owned product detail'),
]
