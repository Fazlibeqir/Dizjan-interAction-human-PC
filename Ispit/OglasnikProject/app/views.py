from django.shortcuts import render, redirect
from .models import Category, Oglas
from .forms import OglasForm


# Create your views here.

def index(request):
    oglasi = Oglas.objects.all()
    return render(request, 'index.html', {'oglasi': oglasi})


def detail(request, oglas_id):
    oglas = Oglas.objects.filter(pk=oglas_id).first()
    return render(request, "details.html", {'oglas': oglas})


def newPro(request):
    if request.method == 'POST':
        form = OglasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OglasForm()
    return render(request, "create.html", {'form': form})
