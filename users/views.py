from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        # this is the POST request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # type of messages:
                # messages.debug()
                # messages.info()
                # messages.success()
                # messages.error()
                # messages.warning()
            messages.success(request, f'Your account has been created, you are now able to login')
            return redirect('login')
    else:
        # this is the GET request
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
