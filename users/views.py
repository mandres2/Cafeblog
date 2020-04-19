from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

def register(request):
    # The first line is asking whether the function was a POST request
    if request.method == 'POST':
        #Create a new form that has the data contained in request.POST
        form = UserRegisterForm(request.POST)
        # Is our form valid?
        if form.is_valid():
            form.save() # This will automatically hash the user's password.
            # If the form data is valid proceed to creating the user and flash a message saying that the account was created
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#This adds functionality to an existing function - which in this case this adds functionality to our profile-view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    #Dictionary with two keys u_form and p_form
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# Message Options

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error