from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    product_type=[
        ('watch','rolex'),
        ('phone','samsung'),
        ('apple','iphone'),
        ('laptop','acer'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pictures/')
    date_added= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=6,choices=product_type)

    def __str__(self):
        return self.name
    