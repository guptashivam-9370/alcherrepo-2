from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'alcher/index.html')

def page1(request):
    return render(request , 'alcher/page1.html')

def page2(request):
    return render(request , 'alcher/page2.html')