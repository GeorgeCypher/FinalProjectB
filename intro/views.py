from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'intro.html'

def baseopen(request):
    return HttpResponse('<h1>Hello World</h1>')