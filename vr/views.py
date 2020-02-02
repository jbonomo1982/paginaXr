from django.shortcuts import render

# Create your views here.

def vr(request):
    return render(request, 'vr/index.html', {})