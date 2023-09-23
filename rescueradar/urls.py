from django.urls import include, path
from django.contrib import admin
from base import views as base_views
from base.views import request_submitted

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', base_views.home, name='home'),
    path('about/', base_views.about, name='about'),
    path('contact/', base_views.contact, name='contact'),
    path('accounts/profile/', base_views.profile, name='profile'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    path('request_submitted/<str:form_submitted>/', base_views.request_submitted, name='request_submitted'),
    path('user_profile/', base_views.user_profile, name='user_profile'),
    path('user_report/', base_views.user_report, name='user_report'),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]