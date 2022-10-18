from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"core/index.html")

def unapagina(request):
    return render(request,"core/unapagina.html")

def otrapagina(request):
    return render(request,"core/otrapagina.html")
