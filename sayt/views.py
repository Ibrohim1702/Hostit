from django.shortcuts import render

# Create your views here.

def index(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )

        ctx = {
            "contact": contact,

        }
    return render(requests, "index.html", ctx)


def about(requests):
    ctx = {

    }
    return render(requests, "about.html", ctx)


def contact(requests):
    ctx = {

    }
    return render(requests, "contact.html", ctx)


def price(requests):
    ctx = {

    }
    return render(requests, "price.html", ctx)


def service(requests):
    ctx = {

    }
    return render(requests, "service.html", ctx)



