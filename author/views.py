from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def author_detail(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('author_detail')
    
    else:
        author_form = forms.AuthorForm()
    return render(request, 'author_detail.html', {'form' : author_form})