from django.shortcuts import render
from .models import HomeWork


def index(request):
    projects = HomeWork.objects.all
    return render(request, 'hw/index.html',
                  {'projects': projects})
