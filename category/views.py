
from django.shortcuts import render, redirect
from . import forms

def category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category')
    
    else:
        category_form = forms.CategoryForm()
    return render(request, 'category.html', {'form' : category_form})
