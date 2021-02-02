from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.

CATEGORIES_CHOICES = (
    ('C','Canned_foods'),
    ('V', 'Vegetables'),
    ('SP', 'Spices'),
    ('BK', 'Bakery')
)

LABEL_CHOICES = (
    ('P','Primary'),
    ('S','Secondary'),
    ('D','Danger'),
    
)
class Products(models.Model):
    title = models.CharField(max_length =30)
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=60)
    price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to = 'images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=60)
    # quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("")