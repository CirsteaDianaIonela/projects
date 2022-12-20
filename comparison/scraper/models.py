from django.db import models

class Products(models.Model):
    objects = None
    product_code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    altex_price = models.CharField(max_length=100)
    active = models.BooleanField(default=1)
    emag_price = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)  #null = True to ImageField will enable it to store empty values as NULL for that table in relational database. blank= True If True, the field is allowed to be blank
    url_altex = models.URLField(null=True, blank=True)  # same as imagiefield
    url_emag = models.URLField(null=True, blank=True)  # same as imagiefield

    def __str__(self):
        return f'{self.product_code}'

#done
