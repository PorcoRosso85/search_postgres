from django.shortcuts import render
from django.views.generic import ListView

from .models import Quote

class QuoteList(ListView):
    model = Quote
    template_name = 'quote.html'
    context_object_name = 'quotes'

    
