from django.urls import path
from .views import index, projects, contact
app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
]
