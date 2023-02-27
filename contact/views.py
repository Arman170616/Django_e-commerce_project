from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # do something with the form data (e.g. send an email)
    else:
        form = ContactForm()
    return render(request, 'Contact/contact.html', {'form': form}) #App_Shop/product_detail.html
