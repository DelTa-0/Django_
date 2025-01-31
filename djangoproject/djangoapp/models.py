from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description=models.TextField(default='')

    def __str__(self):
        return self.name
    
#one to many
class productReview(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.product.name}'
    
#many to many
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=50)
    products=models.ManyToManyField(Products,related_name='stores')

    def __str__(self):
        return self.name
    
#one to one
class productCertificate(models.Model):
    product=models.OneToOneField(Products,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_date=models.DateTimeField()

    def __str__(self):
        return f'certificate for {self.name.product}'