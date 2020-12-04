from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from shop.models import Product
from .forms import AccountCreationForm, SignInForm
from .models import Account


class UserDashboard(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.filter(user=request.user)
        context = {
            'products': products
        }
        return render(request, 'users/dashboard.html', context=context)


class SignUpUser(CreateView):
    model = Account
    form_class = AccountCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('accounts:user dashboard')
    context_object_name = 'form'

    def form_valid(self, form):
        valid = super(SignUpUser, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(username=email, password=password)
        login(self.request, new_user)
        return valid


class SignInUser(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'users/sign_in.html', {'form': form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:user dashboard')
            return render(request, 'users/sign_in.html',
                          {'form': form, 'error': "Account with that email and/or password do not exist."})
        return render(request, 'users/sign_in.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('shop:shop index')
