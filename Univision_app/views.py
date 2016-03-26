from django.shortcuts import render
from .models import User
from .forms import SignUpForm
import datetime
from django.core.validators import validate_email
from django.db import IntegrityError
from django import forms

def home(request):
    
    msg = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
	    # save user info to DB
         

	    try:
		validate_email(form.cleaned_data['email'])
	        try:
		    usr = User.objects.create(name=form.cleaned_data['name'], email=form.cleaned_data['email'], datecreated=datetime.datetime.now())
		    usr.save()
		    msg = 'Thank you for signing up for the mailing list!'
	   	except IntegrityError:
                    msg = 'You are already signed up!'
	    except forms.ValidationError:
	        msg = 'Please enter a valid email.'
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
	    #pass

    # if a GET (or any other method) create a blank form
    else:
        form = SignUpForm()

    return render(request, 'home.tpl', {'form':form, 'msg':msg})

def users(request):
    usrs = User.objects.all()
    return render(request, 'users.tpl', {'usrs':usrs})
