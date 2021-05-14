from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def-define


def testfun1(request):
    return render(request,'index.html')
