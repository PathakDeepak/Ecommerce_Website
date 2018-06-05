from django.http import HttpResponse
from django.shortcuts import render



# def home_page_old(request):
#     return HttpResponse("<h1> Hello World!</h1>");

def home_page(request):
    context = {
        "title": "Home"
    }
    return render(request, "home_page.html", context)
def contact_page(request):
    context = {
        "title": "Contact"
    }
    return render(request, "contact_page.html", context)
def about_page(request):
    context = {
        "title": "About"
    }
    return render(request, "about_page.html", context)
