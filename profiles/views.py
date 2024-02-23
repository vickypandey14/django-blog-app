from django.shortcuts import render, redirect
from . import forms

def profiles(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profiles')
    
    else:
        profile_form = forms.ProfileForm()
    return render(request, 'profiles.html', {'form' : profile_form})

