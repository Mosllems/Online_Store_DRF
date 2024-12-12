from django.shortcuts import render

from .models import Customer

def test(request):
    customers = Customer.objects.all()

    return render(request, "products/test.html", {'customers':customers})