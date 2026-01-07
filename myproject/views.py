from django.shortcuts import render

#home
def homepage(request):
    return render(request,'home.html')

#home
def about(request):
    return render(request,'about.html')