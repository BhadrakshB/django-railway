from django.shortcuts import render

from .forms import InputForm
from .models import Database


# Create your views here.
def view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, 'register.html', context)


def upload(request):
    print(request.POST)
    if 'passenger_senior_citizen' in request.POST.keys():
        passenger_senior_citizen = request.POST['passenger_senior_citizen']
    else:
        passenger_senior_citizen = False

    boarding_place = request.POST['boarding_place']
    destination_place = request.POST['destination_place']
    date_of_travel = request.POST['date_of_travel']
    passenger_name = request.POST['passenger_name']
    passenger_age = request.POST['passenger_age']
    passenger_berth_preference = request.POST['passenger_berth_preference']

    data = Database.objects.create(boarding_place=boarding_place, destination_place=destination_place,
                                   date_of_travel=date_of_travel, passenger_name=passenger_name,
                                   passenger_age=passenger_age, passenger_berth_preference=passenger_berth_preference,
                                   passenger_senior_citizen=passenger_senior_citizen)
    data.save()
    return render(request, 'final.html')
