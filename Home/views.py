from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
def index(request):
    context = {'variable': "This is sent"}
    messages.success(request, "This is a test message.")
    return render(request, "index.html", context)
def about(request):
    return render(request,"about.html")
def services(request):
    return HttpResponse("Services Page")
def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
    return render(request, "contact.html")

  
# Create your views here.
