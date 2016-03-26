from django.shortcuts import render
from .models import User

def home(request):
    if(request.method == 'POST'):
        pass
    return render(request, 'home.tpl', {})
