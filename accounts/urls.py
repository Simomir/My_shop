from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpUser.as_view(), name='signup user'),
    path('signin/', views.SignInUser.as_view(), name='user sign in'),
    path('signout/', views.logout_user, name='sign out'),
    path('dashboard/', views.UserDashboard.as_view(), name='user dashboard'),
    path('edit_info/', views.edit_user_info, name='edit user info'),
    path('delete/', views.delete_user, name='delete user'),
]
