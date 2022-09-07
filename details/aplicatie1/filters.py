import django_filters

from .models import Visualization


class VisualizationFilter(django_filters.FilterSet):

    class Meta:
        model = Visualization
        fields = {'project': ['icontains']}
