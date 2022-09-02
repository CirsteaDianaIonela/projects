from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicatie1.models import Visualization


class VisualizationsView(LoginRequiredMixin, ListView):
    model = Visualization #luat din models si il importam
    template_name = 'aplicatie1/visualizations_index.html'
    queryset = model.objects.filter(active=1)


    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsView, self).get_context_data(*args, **kwargs)
        return data

class CreateVisualizationsView(LoginRequiredMixin, CreateView):
    model = Visualization #luat din models si il importam
    fields = ['project', 'description', 'responsible', 'estimated_duration', 'deadline', 'status', 'percentage', 'comment'] #ce campuri sa aduca din model
    template_name = 'aplicatie1/visualizations_form.html'#template-ul catre care trimitem

    def get_success_url(self):
        return reverse('visualizations:lista_vizualizare') #luat din urls, catre ce pagina sa ne trimita dupa ce adaugam datele

class UpdateVisualizationsView(LoginRequiredMixin, UpdateView):
    model = Visualization #luat din models si il importam
    fields = ['project', 'description', 'responsible', 'estimated_duration', 'deadline', 'status', 'percentage', 'comment'] #ce campuri sa aduca din model
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
    queryset = model.objects.filter(active=0)

    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsInactiveView, self).get_context_data(*args, **kwargs)
        return data
