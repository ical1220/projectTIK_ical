from django.shortcuts import render

# Create your views here.
def feb(request):
    return render(request, 'indexfeb.html')
