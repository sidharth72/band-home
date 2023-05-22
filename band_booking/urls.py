from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin

app_name = 'user'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('band/', include(('band.urls', 'band'), namespace='band')),
    path('venue/', include(('venue.urls', 'venue'))),
    path('booking/', include(('booking.urls', 'booking'))),
    path('shift/', include(('shift.urls', 'shift'))),
    path('admin/', admin.site.urls),
]
