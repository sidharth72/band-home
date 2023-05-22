from django.urls import path, include
from shift import views

urlpatterns = [
	path('', views.ShiftListView.as_view(), name='list'),
]
