from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


def tvshow(request):
    shows = models.TVShow.objects.all()
    return render(request, 'tvshows.html', {'shows_object': shows})


def tvshow_detail(request, id):
    shows = get_object_or_404(models.TVShow, id=id)
    return render(request, 'tvshows_detail.html', {'shows_id': shows})


def add_shows(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Good!')
    else:
        form = forms.ShowForm()
    return render(request, 'addtvshow.html', {'form': form})


def show_update(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated!')
    else:
        form = forms.ShowForm(instance=show_object)
    return render(request, 'tvshow_update.html', {'form': form, 'object': show_object})


def show_delete(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    show_object.delete()
    return HttpResponse('TV Show deleted')
