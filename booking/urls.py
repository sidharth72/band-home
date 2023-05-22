from django.urls import path, include
from django.contrib import admin
from booking import views

booking = [
	path(r'^$', views.BookingDetailView.as_view(), name='detail'),
    path(r'^transition/$', views.BookingTransitionView.as_view(), name='transition'),
    path(r'^change/$', views.BookingUpdateView.as_view(), name='change'),
	path(r'^report/edit/$', views.BookingReportCreateView.as_view(), name='report_edit'),
	path(r'^tecnicalreq/add/$', views.TechnicalRequirementCreateView.as_view(), name='techreq_add'),
]

urlpatterns = [
	path(r'^$', views.BookingListView.as_view(), name='list'),
	path(r'^create/$', views.BookingCreateView.as_view(), name='create'),
	path(r'^(?P<booking>\d+)/', include(booking)),
]
