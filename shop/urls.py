from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.landing, name='landing page'),
    path('all/', views.index, name='shop index'),
    path('create/', views.create_product, name='create product'),
    path('detail/<int:pk>/', views.product_detail, name='product detail'),
    path('edit/<int:pk>/', views.edit, name='edit product'),
    path('delete/<int:pk>/', views.delete, name='delete product'),
]
