from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.navbar,name='navbar'),
    path('homepage',views.homepage,name='homepage'),
    path('experties',views.experties,name='experties'),
    path('productbrand',views.productbrand,name='productbrand'),
    path('footer',views.footer,name='footer'),
    path('buyproducts',views.buyproducts,name='buyproducts'),
    path('gallery',views.gallery,name='gallery'),
    
    path('career',views.career,name='career'),
    path('contact',views.contact,name='contact'),
    path('projectupdates',views.projectupdates,name='projectupdates'),
    path('ongoingprojects',views.ongoingprojects,name='ongoingprojects'),
]