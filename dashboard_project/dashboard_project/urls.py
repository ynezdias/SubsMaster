
from django.urls import path
from dashboard import views
from django.urls import path
#from .views import active_user
from dashboard.views import active_users
#from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/active-users/', views.active_users, name='active_users'),
    #path('active-user/', views.active_users, name='active_users'),
    path('dashboard/expiring-soon/', views.expiring_soon, name='expiring_soon'),
    path('dashboard/inactive-users/', views.inactive_users, name='inactive_users'),
    path('dashboard/expired-users/', views.expired_users, name='expired_users'),
    path('extend-subscription/', views.extend_subscription, name='extend_subscription'),
    path('extend_subscription/<str:user_id>/', views.extend_subscription, name='extend_subscription'),
    #path('dashboard/extend_subscription/', views.extend_subscription, name='extend_subscription'),
    #path('dashboard/extend-subscription/<int:user_id>/', views.extend_subscription, name='extend_subscription'),
    path('toggle_user_status/<int:user_id>/', views.activate_deactivate_user, name='toggle_user_status'),
    #path('dashboard/toggle_user_status/<int:user_id>/', views.activate_deactivate_user, name='toggle_user_status'),
    #path('dashboard/activate-deactivate-user/<int:user_id>/', views.activate_deactivate_user, name='activate_deactivate_user'),
]

'''
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from dashboard.views import DashboardView
from django.http import HttpResponse
from django.urls import reverse
from django.urls import path
from . import views

# Example usage of reversing a URL
#url = reverse('dashboard:url_name')
app_name = 'dashboard'
url = reverse('dashboard')

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    path('active/', views.active_users, name='active_users'),
    path('expiring/', views.expiring_soon_users, name='expiring_soon_users'),
    path('inactive/', views.inactive_users, name='inactive_users'),
    path('admin/', admin.site.urls),
    
]'''

'''app_name = 'dashboard'
#path('dashboard/', include('dashboard.urls', namespace='dashboard')),
#path('example/', views.example_view, name='url_name'),
urlpatterns = [
    path('example/', views.example_view, name='url_name'),
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #path('dashboard/', include('dashboard.urls', namespace='dashboard')),'''
'''from django.urls import path
from . import views
app_name = 'dashboard'
url = reverse('dashboard')
urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', views.dashboard, name='dashboard'),
    path('active/', views.active_users, name='active_users'),
    path('expiring/', views.expiring_soon_users, name='expiring_soon_users'),
    path('inactive/', views.inactive_users, name='inactive_users'),
]
'''