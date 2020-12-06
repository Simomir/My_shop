from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Product
from .forms import ProductForm


class ShopIndex(ListView):
    queryset = Product.available_products.all()
    context_object_name = 'products'
    paginate_by = 8
    template_name = 'shop/index.html'


@login_required
def create_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'shop/products/create.html', {'form': form})
    else:
        form = ProductForm(request.POST, request.FILES, instance=Product())
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('accounts:user dashboard')
        return render(request, 'shop/products/create.html', {'form': form})


@login_required
def edit(request,):
    if request.method == "GET":
        pass
    else:
        pass


@login_required
def delete(request):
    pass


def product_detail(request):
    pass


def landing(request):
    return render(request, 'shop/landing_page.html')
