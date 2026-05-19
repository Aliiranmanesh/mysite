from django.urls import path
from website.views import home
from website.views import about
from website.views import contact

app_name = 'website'
urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact')

]