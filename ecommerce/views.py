from django.shortcuts import render, redirect
from .Forms.form import ContactForm



# def home_page_old(request):
#     return HttpResponse("<h1> Hello World!</h1>");

def home_page(request):
    context = {
        "title": "Home",
        "content": "Welcome to homepage",
    }
    if request.user.is_authenticated:
        context["premium_content"]= "YEAHHHHHHH"
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get('fullName'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact_page.html", context)


def about_page(request):
    context = {
        "title": "About"
    }
    return render(request, "about_page.html", context)


