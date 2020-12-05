from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    products = Product.available_products.all()
    context = {
        'products': products,
    }
    return render(request, 'shop/index.html', context=context)


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
