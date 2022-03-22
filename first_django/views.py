from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return render(req, 'index.html')


def test_example(request):
    return HttpResponse(request, 'Test http response')