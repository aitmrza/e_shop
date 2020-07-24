from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sellers', views.sellers, name='sellers'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('password_change/', views.password_change, name='password_change')
]
