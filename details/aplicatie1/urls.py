#urls secundare ale aplicatii adica o sa vina cu visualizations + delete/add/etc
from django.urls import path, include

from aplicatie1 import views
from .models import Visualization
app_name = 'visualizations'

# from django_downloadview import ObjectDownloadView
# download = ObjectDownloadView.as_view(model=Visualization, file_field='file')
urlpatterns = [

    path('', views.VisualizationsView.as_view(), name='lista_vizualizare'),
    path('adaugare/', views.CreateVisualizationsView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateVisualizationsView.as_view(), name='modifica'), #il duc in index ca sa creez butonul
    path('<int:pk>/delete/', views.delete_visualizations, name='sterge'), #il duc in index ca sa creez butonul
    path('<int:pk>/activeaza/', views.activate_visualizations, name='activeaza'), #il duc in index ca sa creez butonul
    path('vizualizare_inactive', views.VisualizationsInactiveView.as_view(), name='vizualizare_inactive'), #il duc in base ca sa creez tab-ul
    path('all', views.Deadline.as_view(), name='all'), #il duc in base ca sa creez tab-ul
    path('download/', views.download_file, name='download'),
    # path('download//', download, name='download'),

]
