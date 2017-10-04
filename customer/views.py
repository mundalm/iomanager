from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Customer

class IndexView(generic.ListView):
    template_name='customer/index.html'
    context_object_name='all_customers'

    def get_queryset(self):
        return Customer.objects.all()

class DetailView(generic.DetailView):
    model = Customer
    template_name = 'customer/detail.html'

class CustomerCreate(CreateView):
    model = Customer
    fields = ['name', 'docString' ]

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['name', 'docString' ]

class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:index')