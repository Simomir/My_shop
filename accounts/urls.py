from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpUser.as_view(), name='signup user'),
    path('signin/', views.SignInUser.as_view(), name='user sign in'),
    path('signout/', views.logout_user, name='sign out'),
    path('dashboard/', views.UserDashboard.as_view(), name='user dashboard'),
]
