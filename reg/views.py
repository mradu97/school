from django.shortcuts import render
from django.http import HttpResponse

def ho(req):
    return HttpResponse("hello world")

# Create your views here.
def ho1(req):
    return render(req,'ind.html',{'nm':'mradu'})

def sum1(req):
    a=int(req.GET['n1'])
    b=int(req.GET['n2'])
    c=a+b
    return render(req,'result.html',{'ans':c})

def sum(req):
    i=int(req.POST['n1'])
    j=int(req.POST['n2'])
    k=i+j
    return render(req,'result.html',{'ans1':k})
