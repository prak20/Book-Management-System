from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return (res)
def greeting(request):
    s="<h1>Hello and Welcome to first view of testapp</h1><p>This is landing page</p>"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>Website : google.com</p>"
    s+="<p>Mobile : 9910600932</p>"
    s+="<p>Email : prakhar.15it@gmail.com</p>"
    return HttpResponse(s)
def about(request):
    text="this is about page"
    return render(request,'testapp/about.html',{'text':text})
