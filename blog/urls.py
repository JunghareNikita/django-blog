from django.urls import path, include
from . import views

urlpatterns = [
    path('user_signup', views.UserSignup, name='user_signup'),
    path('admin_signup', views.AdminSinup, name='admin_signup'),
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('blog_add', views.BlogAdd, name='blog_add'),
    path('edit_blog/<int:pk>/', views.BlogEdit, name='edit_blog'),
    path('delete_blog/<int:pk>/', views.BlogDelete, name='delete_blog'),
    path('', views.home, name='home'),
]