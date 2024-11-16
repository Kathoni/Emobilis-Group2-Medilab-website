from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm  # Import the form
from .models import Appointment
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm()

    return render(request, 'index.html', {'form': form})

def contact(request):
    data = Appointment.objects.all()
    return render(request, 'contact.html', {'data': data})

def edit(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST,request.FILES,instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment Updated successfully')
            return redirect('contact')
        else:
            messages.error(request, 'Please check form details')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit.html', {'form': form, 'appointment':appointment})

def delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)

    try:
        appointment.delete()
        messages.success(request, 'Appointment Successfully deleted')
    except Exception as e:
        messages.error(request, 'appointment not deleted')

    return redirect('contact')