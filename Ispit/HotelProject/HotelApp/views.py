from django.shortcuts import render, redirect

from .models import Hotels, Room
from .forms import RoomForm


# Create your views here.

def index(request):
    hotels = Hotels.objects.all()
    rooms = Room.objects.filter(bed_number__lte=5, status=True)

    context = {'hotels': hotels, 'rooms': rooms}
    return render(request, "index.html", context=context)


def add(request):
    if request.method == "POST":
        room = RoomForm(request.POST, request.FILES)
        if room.is_valid():
            room.save(commit=False)
            room.status = True
            room.save()
        return redirect('/index')
    else:
        room = RoomForm()
    return render(request, "contactUs.html", {'form': room})
