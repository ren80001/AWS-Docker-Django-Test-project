from django.shortcuts import render

# Create your views here.
def helloworldfunction(request):
    return render(request, 'index.html')
