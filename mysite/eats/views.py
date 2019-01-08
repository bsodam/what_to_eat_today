from django.shortcuts import render, get_object_or_404
from django.views import generic

from eats.models import Restaurant

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'eats/index.html'