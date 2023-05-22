from django.urls import path, include
from django.contrib import admin
from band import views

band = [
	path('', views.BandDetailView.as_view(), name='detail'),
	path('update/', views.BandUpdateView.as_view(), name='update'),
	path('member/add/', views.BandCreateMemberView.as_view(), name='member_add'),
]

urlpatterns = [
	path('', views.BandListView.as_view(), name='list'),
	path('create/', views.BandCreateView.as_view(), name='create'),
	path(r'^(?P<band_pk>\d+)/', include(band)),
	path(r'^(?P<band_slug>[-a-zA-Z0-9]+)/', include(band)),
]
