from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST': # if the calling code is posting new user info
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # must save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created.  Your are now able to log in.')
            return redirect('blog-home')
    else: # if the calling code is simply generating a blank form
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required # decorator declaration
def profile(request):
    if request.method == 'POST': # if the calling code is posting new user info
        print('profile view: post')
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile') # redirect here to avoid post-get-redirect pattern (redundant 'are you sure' message)
    else:
        print('profile view: not post')
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
    