from django.shortcuts import render,HttpResponse
def index(request):
    return render(request,"index.html")
def about(request):
    return HttpResponse("About Page")
def services(request):
    return HttpResponse("Services Page")
def contact(request):
    return HttpResponse("this is Contact Page")

# Create your views here.
