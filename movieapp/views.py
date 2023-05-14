from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    details={'movie_list':movie}
    return render(request,'index.html',details)

def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def edit(request,id):
    movie=Movie.objects.get(id=id)
    form1=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form1':form1,'movie1':movie})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
       # movie.save()
        return redirect('/')
    return render(request,'delete.html')
def show(request,id):
    movie=Movie.objects.get(id=id)
    return render(request,'show.html',{'movie':movie})