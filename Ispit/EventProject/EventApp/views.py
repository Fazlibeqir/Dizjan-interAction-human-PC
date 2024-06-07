from datetime import datetime
from django.shortcuts import render, redirect
from .models import Event, Bands, EventBands
from .forms import EventForm


# Create your views here.

def index(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "index.html", context)


def eventAdd(request):
    form = EventForm()
    events_in_future = Event.objects.filter(date__gte=datetime.now().date()).all()
    extra_context = {'form': form, 'all_events': events_in_future}
    if request.method == 'POST':
        form_data = EventForm(request.POST, request.FILES)
        if form_data.is_valid():
            form = form_data.save(commit=False)
            form.poster = form_data.cleaned_data['poster']
            form.user = request.user
            form.save()
            bands = form_data.cleaned_data['bands']
            band_list = bands.split(',')
            for band in band_list:
                band_obj = Bands.objects.filter(name=band).first()
                if band_obj:
                    band_obj.events_held = band_obj.events_held + 1
                    band_obj.save()
                    EventBands.objects.create(bands=band_obj, event=form)
            return redirect('index')
    return render(request, "eventFrom.html", context=extra_context)
