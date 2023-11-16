from django.db import models
import os
import uuid

def product_image_path(instance,filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join("product",filename)

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(null=True,upload_to=product_image_path)
    createdOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
