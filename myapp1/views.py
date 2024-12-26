from django.shortcuts import render
from .models import animalwebsite

# Create your views here.

# this is for main.html view====------------------------------
def main(request):
    return render(request,'main.html')

# this is for modelsmain.html view====------------------------------
def models(request):
    a=animalwebsite.objects.all()
    return render(request,'modelmaim.html',context={'fun':a})


