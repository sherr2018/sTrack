from django.shortcuts import render
from django.http import HttpResponse
from .models import employees
# Create your views here.


def index(request):
    emList=employees.objects.order_by('id')
    alist='\n</br>'.join([q.name for q in emList]).join([q.username for q in emList])
    return HttpResponse(alist)