from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


def demo(request):
        obj=place.objects.all()
        obj1=team.objects.all()
        return render(request, "index.html",{'result':obj,'res':obj1})


