from django.shortcuts import render

# Create your views here.


def tutorials(request):
    return render(request, 'tutorials/tutorials.html')
