from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models, forms


# def tvshow(request):
#     shows = models.TVShow.objects.all()
#     return render(request, 'tvshows.html', {'shows_object': shows})
class TVShowView(generic.ListView):
    template_name = 'tvshows.html'
    queryset = models.TVShow.objects.all()

    def get_queryset(self):
        return models.TVShow.objects.all()


# def tvshow_detail(request, id):
#     shows = get_object_or_404(models.TVShow, id=id)
#     return render(request, 'tvshows_detail.html', {'shows_id': shows})
class TVShowDetailView(generic.DetailView):
    template_name = 'tvshows_detail.html'

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=shows_id)


# def add_shows(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Good!')
#     else:
#         form = forms.ShowForm()
#     return render(request, 'addtvshow.html', {'form': form})

class TVShowCreateView(generic.CreateView):
    template_name = 'addtvshow.html'
    form_class = forms.ShowForm
    queryset = models.TVShow.objects.all()
    success_url = '/shows/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TVShowCreateView, self).form_valid(form=form)


# def show_update(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Updated!')
#     else:
#         form = forms.ShowForm(instance=show_object)
#     return render(request, 'tvshow_update.html', {'form': form, 'object': show_object})

class TVShowUpdateView(generic.UpdateView):
    template_name = 'tvshow_update.html'
    form_class = forms.ShowForm
    success_url = '/shows/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)

    def form_valid(self, form):
        return super(TVShowUpdateView, self).form_valid(form=form)


# def show_delete(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     show_object.delete()
#     return HttpResponse('TV Show deleted')

class TVShowDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/shows/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)
