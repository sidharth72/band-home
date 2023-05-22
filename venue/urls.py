from django.urls import path, include
from venue import views

venue = [
	path(r'^$', views.VenueDetailView.as_view(), name='detail'),
]

urlpatterns = [
    path(r'^$', views.VenueListView.as_view(), name='list'),
	path(r'^(?P<venue_pk>\d+)/', include(venue)),
	path(r'^(?P<venue_slug>[-a-zA-Z0-9]+)/', include(venue)),
]
