from main.models import Vehicle
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .NetworkHelper import NetworkHelper

api = NetworkHelper(
    base_url="http://127.0.0.1:3000/api/",
    username="llesya",
    password="llesya2006"

)
def settlements_api_list(request):
    settlements = api.get_settlements()
    return render(request, 'webapp/settlements_api_list.html', {'settlements': settlements})

def settlement_api_delete(request, pk):
    if request.method == 'POST':
        api.delete_settlement(pk)
    return redirect('settlements_api_list')

def persons_api_list(request):
    persons = api.get_persons()
    return render(request, 'webapp/persons_api_list.html', {'persons': persons})

def person_api_delete(request, pk):
    if request.method == 'POST':
        api.delete_person(pk)
    return redirect('persons_api_list')

def vehicle_list (request):
    vehicles = Vehicle.objects.all()
    return render(request, 'webapp/vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail (request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'webapp/vehicle_detail.html', {'vehicle': vehicle})


class VehicleCreateView(CreateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle_list')
    template_name = 'webapp/vehicle_form.html'


class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle_list')
    template_name = 'webapp/vehicle_form.html'


class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')
    template_name = 'webapp/vehicle_delete.html'
