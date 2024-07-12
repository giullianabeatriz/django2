from django.shortcuts import render

# Create your views here.
def index (request):
    print("consgui chegar na view")
    return render(request, "index.html")