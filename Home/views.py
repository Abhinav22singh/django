from django.shortcuts import render,HttpResponse
def index(request):
    return HttpResponse("Home Page")
def about(request):
    return HttpResponse("About Page")
def services(request):
    return HttpResponse("Services Page")
def contact(request):
    return HttpResponse("Contact Page")

# Create your views here.
