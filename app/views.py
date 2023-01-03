from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'a':[12,344,56] , 'b':[15,]}
    return render(request,'loop.html',d) 
def looping(request):
    a={'b':['hello world']}
    return render(request,'loop.html')
