from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Equipment

class IndexView(generic.ListView):
    template_name='manageio/index.html'
    context_object_name='all_equipment'

    def get_queryset(self):
        return Equipment.objects.all()

class DetailView(generic.DetailView):
    model = Equipment
    template_name = 'manageio/detail.html'

class EquipmentCreate(CreateView):
    model = Equipment
    fields = ['name', 'tag', 'tfmPrefix', 'docString' ]

class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ['name', 'tag', 'tfmPrefix', 'docString' ]

class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('manageio:index')

