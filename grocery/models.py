# from django.db import models
# from django.db.models.signals import post_save
# from django.conf import settings
# from django.dispatch  import receiver
# from django.shortcuts import reverse
# from django.contrib.auth.models import User
# # Create your models here.

# CATEGORIES_CHOICES = (
#     ('C','Canned_foods'),
#     ('V', 'Vegetables'),
#     ('SP', 'Spices'),
#     ('BK', 'Bakery')
# )

# LABEL_CHOICES = (
#     ('P','primary'),
#     ('S','secondary'),
#     ('D','danger'),
    
# )
# class Product(models.Model):
#     title = models.CharField(max_length =30)
#     category = models.CharField(choices=CATEGORIES_CHOICES, max_length=60)
#     price = models.FloatField()
#     description = models.TextField()
#     slug = models.SlugField(max_length=150)
#     image = models.ImageField(upload_to = 'images/')
#     labels = models.CharField(choices=LABEL_CHOICES, max_length=60)
#     quantity = models.IntegerField(default=1)
    
#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse("grocery:products", kwargs={'slug': self.slug})
    
#     def get_add_to_cart_url(self):
#      return reverse("grocery:add-to-cart", kwargs={'slug': self.slug})

  
#     @classmethod
#     def search_by_title(cls,search_term):
#         product = cls.objects.filter(title__icontains=search_term)
#         return product
    
# class OrderProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title
# class Order(models.Model):   
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(OrderProduct)
#     pub_date = models.DateTimeField(auto_now_add=True,null=True)
#     ordered =  models.BooleanField(default=False)
#     ordered_delete = models.DateTimeField(auto_now_add=True,null=True)
    
#     def __str__(self):
#         return self.user.username
        