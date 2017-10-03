from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Customer

class IndexView(generic.ListView):
    template_name='customer/index.html'
    context_object_name='all_customers'

    def get_queryset(self):
        return Customer.objects.all()