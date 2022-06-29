from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from administrativo.models import *
from administrativo.forms import *


def index(request):

    edificios = Edificio.objects.all()

    informacion_template = {'edificios': edificios,
                            'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)
