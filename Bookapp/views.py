from django.shortcuts import render
from Bookapp.forms import NewBookForm,SearchForm
from Bookapp import models
from django.http import HttpResponse,HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/Bookapp/login/")
def newBook(request):
    form=NewBookForm()
    res=render(request,'Bookapp/new_book.html',{'form':form})
    return res
@login_required(login_url="/Bookapp/login/")
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="<h1 style='text-align: center; color: Tomato; font-family: arial, sans-serif; background-color:DodgerBlue;'>Record Stored in DB </h1><br><br><h2><a href='/Bookapp/view-books'  style='text-align: center; color: #999999;'>View All Books</a></h2>"
    return HttpResponse(s)
@login_required(login_url="/Bookapp/login/")
def viewBooks(request):
    books=models.Book.objects.all()
    username=request.session['username']
    res=render(request,'Bookapp/view_book.html',{'books':books,'username':username})
    return res
@login_required(login_url="/Bookapp/login/")
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'Bookapp/edit_book.html',{'form':form,'book':book})
    return res
@login_required(login_url="/Bookapp/login/")
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('Bookapp/view-books')
@login_required(login_url="/Bookapp/login/")
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('Bookapp/view-books')
@login_required(login_url="/Bookapp/login/")
def searchBook(request):
    form=SearchForm()
    res=render(request,'Bookapp/search_book.html',{'form':form})
    return res
@login_required(login_url="/Bookapp/login/")
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'Bookapp/search_book.html',{'form':form,'books':books})
    return res
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            request.session['username']=username
            return HttpResponseRedirect('/Bookapp/view-books/')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'Bookapp/user_login.html',data)
            return res
    else:
        return render(request,'Bookapp/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('Bookapp/login/')
