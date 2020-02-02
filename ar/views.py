from django.shortcuts import render

# Create your views here.
def ar(request):
    return render(request, 'ar/index.html', {})