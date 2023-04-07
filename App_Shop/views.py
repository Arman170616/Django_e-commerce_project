from django.shortcuts import render


#import views
from django.views.generic import ListView, DetailView

#models
from App_Shop.models import Product, Category

#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(ListView):
    model = Product
    Categories = Category.objects.all()
    print(Categories)
    template_name = 'App_Shop/home.html'
    # return value of get_context_data is passed to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.Categories
        return context

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'

