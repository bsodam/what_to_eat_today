from django.shortcuts import render, get_object_or_404
from django.views import generic

from eats.models import Restaurant

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'eats/index.html'

class ListView(generic.ListView):
    template_name = 'eats/list.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.order_by('id')

class RestaurantCreate(generic.CreateView):
    model = Restaurant
    fields = ['restaurant_name', 'category', 'address', 'info']
    success_url = '/eats/list'