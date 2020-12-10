from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import ProductForm
from .models import Product


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
def delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.user.id == request.user.id:
        product.delete()
        return redirect('shop:own products')
    return redirect('shop:shop index', {'message': "You tried to access content that belongs to another person."})


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/products/detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs['pk']
        return get_object_or_404(Product, id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = f'{self.object.user.first_name} {self.object.user.last_name}' \
            if self.object.user.first_name and self.object.user.last_name else f'{self.object.user.username}'
        # I know I can make a function inside the model and stuff about getting the name
        # but just wanted you to see I know where stuff comes from.
        other_products = Product.objects.filter(user_id=self.object.user.id)
        context['name'] = name
        context['other_products'] = other_products
        return context


def landing(request):
    return render(request, 'shop/landing_page.html')


class UserOwnedProducts(ListView, LoginRequiredMixin):
    template_name = 'shop/user_owned_products.html'
    model = Product
    paginate_by = 8
    context_object_name = 'own_products'

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id)


class UserOwnProductDetail(DetailView, LoginRequiredMixin):
    model = Product
    template_name = 'shop/own_product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        product_id = self.kwargs['pk']
        return get_object_or_404(Product, id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        can_see_and_modify = self.request.user.id == self.object.user.id
        context['it_can'] = can_see_and_modify
        return context
