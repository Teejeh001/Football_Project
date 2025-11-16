from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('arena/', views.arena, name='arena'),
    path('booking/', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('booking/', views.booking, name='booking'),
    path('logout/', views.logout, name='logout'),
    path('payment/', views.payment, name='payment'),
    path('profile/', views.profile, name='profile'),
]