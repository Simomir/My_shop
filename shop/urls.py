from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='shop index'),
    path('create/', views.create_product, name='create product'),
]
