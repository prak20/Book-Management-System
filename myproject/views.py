from django.http import HttpResponse
from django.shortcuts import redirect

def myhome(request):
    return redirect('/Bookapp/login')
