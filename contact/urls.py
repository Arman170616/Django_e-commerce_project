from django.urls import path
# from contact.views import contact_view
from .views import contact_view, search_view

urlpatterns = [
    path('', contact_view, name='contact'),
    path('search/', search_view, name='search'),
]
