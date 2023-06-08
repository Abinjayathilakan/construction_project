from django.shortcuts import render

# Create your views here.
def navbar(request):
    return render(request,'base.html')

def homepage(request):
    return render(request,'homepage2.html')

def experties(request):
    return render(request,'experties.html')

def productbrand(request):
    return render(request,'productbrand2.html')

def footer(request):
    return render(request,'footer.html')

def buyproducts(request):
    return render(request,'buyproducts.html')

def gallery(request):
    return render(request,'gallery.html')

def career(request):
    return render(request,'career.html')

def contact(request):
    return render(request,'contact2.html')

def projectupdates(request):
    return render(request,'ongoingprojects.html')

def ongoingprojects(request):
    return render(request,'ongoingprojects.html')

def navbar2(request):
    return render(request,'navbar3.html')

def aboutus(request):
    return render(request,'aboutus.html')

def whychooseus(request):
    return render(request,'whychooseus.html')

def partners(request):
    return render(request,'partners.html')