from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login

from authentication.forms import RegistrationForm

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
