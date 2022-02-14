from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,"index.html")

def index_2(request):
    return render(request,"index.html")

def shop(request):
    return render(request,"shop.html")

def contact(request):
    return render(request,"contact.html")

def testimonial(request):
    return render(request,"testimonial.html")
def why(request):
    return render(request,"why.html")