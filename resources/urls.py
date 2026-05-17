from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_resource, name='upload'),
    path('pending-resources/', views.pending_resources, name='pending_resources'),
    path('approve-resource/<int:resource_id>/', views.approve_resource, name='approve_resource'),
    path('delete-resource/<int:resource_id>/', views.delete_resource, name='delete_resource'),
    path('browse/', views.browse_resources, name='browse'),
    path('resource/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('my-uploads/', views.my_uploads, name='my_uploads'),
    path('profile/', views.profile_view, name='profile'),
]

