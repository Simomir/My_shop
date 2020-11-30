from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from .forms import AccountCreationForm
from .models import Account


class UserDashboard(View):
    @login_required
    def get(self, request):
        return render(request, 'users/dashboard.html')

    def post(self, request):
        pass


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
