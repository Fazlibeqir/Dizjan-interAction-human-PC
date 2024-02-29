from django.shortcuts import render
from .models import MyModel


# Create your views here.

def index(request):
    my_object = MyModel.objects.all()
    return render(request, 'index.html', {'my_object': my_object})
