from django.urls import path
from website.views import home
from website.views import about
from website.views import contact

urlpatterns = [
    path('', home),
    path('about', about),
    path('contact', contact)

]