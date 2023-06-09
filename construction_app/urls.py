from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.homepage,name='homepage'),
    path('navbar',views.navbar,name='navbar'),
    path('experties',views.experties,name='experties'),
    path('productbrand',views.productbrand,name='productbrand'),
    path('footer',views.footer,name='footer'),
    path('buyproducts',views.buyproducts,name='buyproducts'),
    path('gallery',views.gallery,name='gallery'),
    
    path('career',views.career,name='career'),
    path('contact',views.contact,name='contact'),
    path('projectupdates',views.projectupdates,name='projectupdates'),
    path('ongoingprojects',views.ongoingprojects,name='ongoingprojects'),
    path('navbar2',views.navbar2,name='navbar2'),
    path('aboutus',views.aboutus,name='aboutus'),
    
    path('whychooseus',views.whychooseus,name='whychooseus'),
    path('partners',views.partners,name='partners'),
]