from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tellhi(reqest):
    return HttpResponse('Hello World')