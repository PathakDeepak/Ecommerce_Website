from django.shortcuts import render
from .Forms.form import ContactForm, LoginForm



# def home_page_old(request):
#     return HttpResponse("<h1> Hello World!</h1>");

def home_page(request):
    context = {
        "title": "Home"
    }
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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user is logged in?")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/login_page.html", context)

def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register_page.html", {})
