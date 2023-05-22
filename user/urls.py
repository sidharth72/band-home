from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path
from user import views

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('password/', views.PasswordChangeView.as_view(), name='changepassword'),
]
