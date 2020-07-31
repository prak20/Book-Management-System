from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showTest(request):
    que="Who developed C"
    a="Ken Thompson"
    b="Dennis Ritchie"
    c="Bjarne Stroustrope"
    d="Prakhar Agarwal"
    level="easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(resquest):
    s="<h1>This is ShowResult page</h1>"
    return HttpResponse(s)
