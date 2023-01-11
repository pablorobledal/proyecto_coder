from django.shortcuts import render

# Create your views here.
def pablitoputo(request):
    return render(request, 'AppUsers/templates/registro.html')