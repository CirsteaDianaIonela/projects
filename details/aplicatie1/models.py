from django.db import models

status_choices = (("Started", "Started"), ("Done", "Done"), ("Not started", "Not started"))
percentage_choices = (("0%", "0%"), ("10%", "10%"), ("20%", "20%"), ("30%", "30%"), ("40%", "40%"), ("50%", "50%"), ("60%", "60%"),
                      ("70%", "70%"), ("80%", "80%"), ("90%", "90%"), ("100%", "100%"))

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



    def __str__(self):
        return f'{self.project} - {self.description} - {self.responsible} - {self.deadline}'\
               f'- {self.status} - {self.percentage} - {self.comment} - {self.file}'

