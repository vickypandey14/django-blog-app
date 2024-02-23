# musicians_directory/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

def musician_create_or_update(request, musician_id=None):
    musician = get_object_or_404(Musician, pk=musician_id) if musician_id else None
    album = Album()

    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance=musician)
        album_form = AlbumForm(request.POST, instance=album)

        if musician_form.is_valid() and album_form.is_valid():
            musician = musician_form.save()
            album.musician = musician
            album = album_form.save()

            return redirect('musician_list')
    else:
        musician_form = MusicianForm(instance=musician)
        album_form = AlbumForm(instance=album)

    return render(request, 'musician_form.html', {'musician_form': musician_form, 'album_form': album_form})

def musician_delete(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    musician.delete()
    return redirect('musician_list')
