from django.db import models

status_choices = (("Started", "Started"), ("Done", "Done"), ("Not started", "Not started"))
percentage_choices = (
("0%", "0%"), ("10%", "10%"), ("20%", "20%"), ("30%", "30%"), ("40%", "40%"), ("50%", "50%"), ("60%", "60%"),
("70%", "70%"), ("80%", "80%"), ("90%", "90%"), ("100%", "100%"))
from django.contrib.auth.models import User

# Create your models here.
class Visualization(models.Model):
    project = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    responsible = models.CharField(max_length=100)
    deadline = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=status_choices, default="Not started")
    percentage = models.CharField(max_length=20, choices=percentage_choices, default="0%")
    comment = models.CharField(max_length=1000, default="To be modified")
    active = models.BooleanField(default=0)
    file = models.FileField(upload_to='store/', default="No file")
    # abc = models.CharField(max_length=100, default="Empty") #creez un camp nou, fac makemigrations, si apare la migrations 0002, apoi vreau sa sterg acest camp, rulez make migrations, apare 0003 si imi spune ca le-a sters
    #daca adaug un camp noi si ii dau migrate, in maria db ar treubi sa vad noul camp in tabelul meu describe aplicatie1_visualization, in maria db: describe describe aplicatie1_visualization
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # read about ORM; One-to-Many relations, Many-to-Many, One-to-One. Normal form 3.
    # create a relation between Visualization model and auth_user model.

    def __str__(self):
        return f'{self.project} - {self.description} - {self.responsible} - {self.deadline}' \
               f'- {self.status} - {self.percentage} - {self.comment} - {self.file}'
