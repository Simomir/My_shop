from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpUser.as_view(), name='signup user'),
    path('dashboard/', views.UserDashboard.as_view(), name='user dashboard'),
]
