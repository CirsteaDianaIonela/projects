
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .filters import VisualizationFilter
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from aplicatie1.models import Visualization


class VisualizationsView(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'aplicatie1/visualizations_index.html'
    paginate_by = 4
    queryset = model.objects.filter(active=1).order_by('project')
    context_object_name = 'visualizations'

    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsView, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

class CreateVisualizationsView(LoginRequiredMixin, CreateView):
    model = Visualization
    fields = ['project', 'description', 'responsible', 'deadline', 'status', 'percentage', 'comment', 'file'] #ce campuri sa aduca din model
    template_name = 'aplicatie1/visualizations_form.html'#template-ul catre care trimitem

    def get_success_url(self):
        return reverse('visualizations:lista_vizualizare') #luat din urls, catre ce pagina sa ne trimita dupa ce adaugam datele

class UpdateVisualizationsView(LoginRequiredMixin, UpdateView):
    model = Visualization #luat din models si il importam
    fields = ['project', 'description', 'responsible', 'deadline', 'status', 'percentage', 'comment', 'file'] #ce campuri sa aduca din model
    template_name = 'aplicatie1/visualizations_form.html'#template-ul catre care trimitem


    def get_success_url(self):
        return reverse('visualizations:lista_vizualizare') #luat din urls, catre ce pagina sa ne trimita dupa ce adaugam datele

@login_required
def delete_visualizations(request, pk):
    Visualization.objects.filter(id=pk).update(active=0)
    return redirect('visualizations:lista_vizualizare')


@login_required
def activate_visualizations(request, pk):
    Visualization.objects.filter(id=pk).update(active=1)
    return redirect('visualizations:lista_vizualizare')

class VisualizationsInactiveView(LoginRequiredMixin, ListView):
    model = Visualization #luat din models si il importam
    template_name = 'aplicatie1/visualizations_index.html'
    paginate_by = 4
    queryset = model.objects.filter(active=0).order_by('project')
    context_object_name = 'visualizations'

    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsInactiveView, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data


from django.db.models import DurationField, F, ExpressionWrapper
from django.db.models.functions import ExtractDay
from django.utils import timezone
import requests

class Deadline(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'aplicatie1/visualizations_index.html'
    # queryset = model.objects.filter(created__gte=Visualization.deadline - datetime.timedelta(days=7))
    # queryset = model.objects.filter(created__gte=Visualization.deadline(days=7))
    # queryset = model.objects.filter(active=1)
    # visualization = model.objects.all()
    # visualization_filter = VisualizationFilter(requests.get, queryset=visualization)
    # context = {'visualization_filter': visualization_filter}
    paginate_by = 4
    context_object_name = 'visualizations'
    queryset = model.objects.order_by('project')
    def get_context_data(self, *args, **kwargs):
        data = super(Deadline, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

