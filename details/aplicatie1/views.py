import mimetypes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from .filters import VisualizationFilter
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from aplicatie1.models import Visualization
from .functions import handle_uploaded_file
import os


class VisualizationsView(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'aplicatie1/visualizations_index.html'
    # paginate_by = 4
    today = datetime.date.today()
    queryset = model.objects.filter(active=1).filter(deadline__gte=today).order_by('project')
    context_object_name = 'visualizations'

    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsView, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

class CreateVisualizationsView(LoginRequiredMixin, CreateView):
    model = Visualization
    fields = ['project', 'description', 'responsible', 'deadline', 'status', 'percentage', 'comment', 'file', 'author'] #ce campuri sa aduca din model
    template_name = 'aplicatie1/visualizations_form.html'#template-ul catre care trimitem

    def index(request):
        if request.method == 'POST':
            abc = Visualization(request.POST, request.FILES)
            if abc.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponse("File uploaded successfuly")
        else:
            abc = Visualization()
            return render(request, "visualizations_form.html", {'form': abc})
    def get_success_url(self):
        return reverse('visualizations:lista_vizualizare') #luat din urls, catre ce pagina sa ne trimita dupa ce adaugam datele

class UpdateVisualizationsView(LoginRequiredMixin, UpdateView):
    model = Visualization #luat din models si il importam
    fields = ['project', 'description', 'responsible', 'deadline', 'status', 'percentage', 'comment', 'file', 'author'] #ce campuri sa aduca din model
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
    # paginate_by = 4
    today = datetime.date.today()
    queryset = model.objects.filter(active=0).filter(deadline__gte=today).order_by('project')
    context_object_name = 'visualizations'

    def get_context_data(self, *args, **kwargs):
        data = super(VisualizationsInactiveView, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

from datetime import timedelta

class Deadline(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'aplicatie1/visualizations_index.html'
    today = datetime.date.today()
    next = datetime.date.today() + timedelta(days=7)
    queryset = model.objects.filter(deadline__lte=next).filter(deadline__gte=today)
    # print(queryset)
    # paginate_by = 4
    context_object_name = 'visualizations'

    def get_context_data(self, *args, **kwargs):
        data = super(Deadline, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

class Expired(LoginRequiredMixin, ListView):
    model = Visualization
    template_name = 'aplicatie1/visualizations_index.html'
    today = datetime.date.today()
    try:
        # date = Visualization.objects.values('deadline').first()['deadline']
        queryset = model.objects.filter(deadline__lte=today)
        # print(queryset)
        # paginate_by = 4
        context_object_name = 'visualizations'
    except Exception:
        print("eroare")

    def get_context_data(self, *args, **kwargs):
        data = super(Expired, self).get_context_data(*args, **kwargs)
        data['filter'] = VisualizationFilter(self.request.GET, queryset=self.get_queryset())
        return data

def download_file(request, filename=''):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/media/store/' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return redirect('visualizations:lista_vizualizare')
