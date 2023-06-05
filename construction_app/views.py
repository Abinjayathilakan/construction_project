from django.shortcuts import render

# Create your views here.
def navbar(request):
    return render(request,'navbar3.html')

def homepage(request):
    return render(request,'homepage.html')

def experties(request):
    return render(request,'experties.html')

def productbrand(request):
    return render(request,'productbrand.html')

def footer(request):
    return render(request,'footer.html')

def buyproducts(request):
    return render(request,'buyproducts.html')

def gallery(request):
    return render(request,'gallery.html')

def career(request):
    return render(request,'career.html')

def contact(request):
    return render(request,'contact.html')

def projectupdates(request):
    return render(request,'projectupdates.html')

def ongoingprojects(request):
    return render(request,'ongoingprojects.html')