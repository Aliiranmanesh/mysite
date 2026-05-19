from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'website/index.html')

def about(requests):
    return render(requests, 'website/about.html')

def contact(requests):
    return render(requests, 'website/contact.html')