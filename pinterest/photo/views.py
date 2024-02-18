from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pins.models import Pin

# Create your views here.
@login_required
def home(request):
    pins = Pin.objects.all()
    content = {
        'pins':pins
    }
    return render(request,'home.html',content)