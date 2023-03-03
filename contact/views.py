from django.shortcuts import render
from .forms import ContactForm
from App_Shop.models import Product

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # do something with the form data (e.g. send an email)
    else:
        form = ContactForm()
    return render(request, 'Contact/contact.html', {'form': form}) #App_Shop/product_detail.html



def search_view(request):
    query = request.GET.get('query', '')
    posts = Product.objects.filter(status = Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'Contact/search.html', {'query': query, 'posts': posts})