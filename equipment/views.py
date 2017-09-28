"""View definitions for Equipment app"""

from django.shortcuts import render, get_object_or_404
from .models import Equipment, Feature

def index(request):
    """Gets all registered equipment and returns it to template"""
    all_equipment = Equipment.objects.all()
    return render(request, 'equipment/index.html', {'all_equipment': all_equipment})

def detail(request, equipment_id):
    """Tries to get equipment with specified equipment_id. Returns either object or 404"""
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    return render(request, 'equipment/detail.html', {'equipment': equipment})

def tested(request, equipment_id):
    """Marks feature as tested"""
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    try:
        selected_feature = equipment.feature_set.get(pk=request.POST['feature'])
    except(KeyError, Feature.DoesNotExist):
        return render(request, 'equipment/detail.html', {
            'equipment': equipment,
            'error_message': "You did not select a valid feature"
    })
    else:
        selected_feature.is_tested = True
        selected_feature.save()
        return render(request, 'equipment/detail.html', {'equipment': equipment})

