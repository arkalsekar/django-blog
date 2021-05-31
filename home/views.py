# Views for  Home App
from home.models import Contact
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from blog.models import Post

# Create your views here.
def index(request):
    latest_post = Post.objects.first()
    messages.info(request, "This is just a Demo Website")
    context = {'alposts': latest_post}
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')    

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        if len(name) < 3 or len(email) < 3 or len(message) < 3:
            messages.error(request, "Please fill the form correctly, Make sure all the fields are more then 3")
        else:
            form = Contact(name=name, email=email, message=message)
            form.save()
            messages.info(request, "Your form has been submitted successfully")
    return render(request, 'home/contact.html')    