from django.db import models

# Create your models here.
class Visualization(models.Model):
    project = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    responsible = models.CharField(max_length=100)
    active = models.BooleanField(default=0)

    def __str__(self):
        return f'{self.project} - {self.description} - {self.responsible}'

