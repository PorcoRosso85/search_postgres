from django.shortcuts import render
from django.views.generic import ListView
#from django.contrib.postgres.search import 
from django.db.models import Q


from .models import Quote

class QuoteList(ListView):
    model = Quote
    template_name = 'quote.html'
    context_object_name = 'quotes'

    
class SearchResultsList(ListView):
    model = Quote
    template_name = 'search.html'
    context_object_name = 'quotes'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.filter(
            Q(name__icontains=query) | Q(quote__icontains=query)
        )
