from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Equipment

class IndexView(generic.ListView):
    template_name='equipment/index.html'
    context_object_name='all_equipment'

    def get_queryset(self):
        return Equipment.objects.all()

class DetailView(generic.DetailView):
    model = Equipment
    template_name = 'equipment/detail.html'

class EquipmentCreate(CreateView):
    model = Equipment
    fields = ['name']

