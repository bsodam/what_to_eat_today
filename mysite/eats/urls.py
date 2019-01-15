from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'eats'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('list/', views.ListView.as_view(), name='list'),
    path('add/', views.RestaurantCreate.as_view(), name='add'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.UserCreateView.as_view(), name='signup' ),
    path('registered/', views.RegisterdView.as_view(), name='registered')
]