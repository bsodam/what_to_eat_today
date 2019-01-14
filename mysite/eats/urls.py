from django.urls import path
from . import views

app_name = 'eats'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('list/', views.ListView.as_view(), name='list'),
    path('add/', views.RestaurantCreate.as_view(), name='add'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]