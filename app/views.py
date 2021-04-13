from django.shortcuts import render
from app.models import Flower

# Create your views here.

def home (request):
    flowers = Flower.objects.all()
    return render(request , 'home.html', {'flowers':flowers})