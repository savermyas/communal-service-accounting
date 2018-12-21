from django.template.response import TemplateResponse
from .models import Apartment

fixtures = ['fixtures/test.json']

def index(request):
    return TemplateResponse(request, 'index.html', {"apartments": [
    apartment for apartment in Apartment.objects.all()
    ]})