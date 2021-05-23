from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def-define


def testfun1(request):
   return render(request,'calculator17.html')
def testfun2(request):
    return render(request,'calc.html')
def testfun3(request):
    return render(request,'form.html')
