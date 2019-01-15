from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from eats.models import Restaurant

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'eats/index.html'

class ResultView(generic.ListView):
    template_name = 'eats/result.html'
    context_object_name = 'random_restaurant'

    def get_queryset(self):
        return Restaurant.objects.order_by('?').first()


class DeleteView(generic.DeleteView):
    model = Restaurant
    success_url = '/eats/list'


class ListView(LoginRequiredMixin, generic.ListView):
    template_name = 'eats/list.html'
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return Restaurant.objects.order_by('id')

class RestaurantCreate(generic.CreateView):
    model = Restaurant
    fields = ['restaurant_name', 'category', 'address', 'info']
    success_url = '/eats/list'

class UserCreateView(generic.CreateView):
    template_name = 'eats/signup.html'
    form_class = UserCreationForm
    success_url = '/eats/registered'

class RegisterdView(generic.TemplateView):
    template_name = 'eats/registered.html'

@login_required
def profile(request):
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
    return render(request, 'eats/profile.html', context={'data': data})
