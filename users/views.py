from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})
