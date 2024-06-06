from django.shortcuts import render,redirect
from .models import Supplements
from .forms import SupplementForm


# Create your views here.


def index(request):
    supplements = Supplements.objects.filter().all()
    return render(request, 'index.html', {'supplements': supplements})


def addSupplements(request):
    if request.method == 'POST':
        form = SupplementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SupplementForm()
    return render(request, "supplementsForm.html", {'form': form})


def detailSupplements(request, supp_id):
    supplement = Supplements.objects.filter(id=supp_id).first()
    return render(request, "supplementsDetails.html", {'supplement': supplement})
