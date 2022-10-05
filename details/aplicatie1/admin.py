from django.contrib import admin
from .models import Visualization
@admin.register(Visualization)
class VisualizationAdmin(admin.ModelAdmin):
    list_display = ("project", "description")


# Register your models here.
