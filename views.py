from django.http import HttpResponse
from django.shutcuts import redirect
def index(request):
    return HttpResponse('index')

def login(request):
    pass
