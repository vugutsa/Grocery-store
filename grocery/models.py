from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch  import receiver
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.
CATEGORIES_CHOICES = (
    ('Canned','Canned_foods'),
    ('Vegies', 'Vegetables'),
    ('Spice', 'Spices'),
    ('Bakery', 'Bakery')
)
ADDRESS_CHOICES = (
    ('Billing', 'Billing'),
)
class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name       

class Product(models.Model):
    title = models.CharField(max_length =30)
    category = models.CharField(choices=CATEGORIES_CHOICES, max_length=60)
    price = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(max_length=150)
    image = models.ImageField(upload_to = 'images/')
    quantity = models.IntegerField(default=1)
    digital = models.BooleanField(default=False,null=True, blank=True)
    def __str__(self):
        return self.title
    @classmethod
    def search_by_title(cls,search_term):
        product = cls.objects.filter(title__icontains=search_term)
        return product
    @classmethod
    def get_product(cls,id):
        try:
            product = Product.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return Product
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Order(models.Model): 
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)  
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    ordered =  models.BooleanField(default=False)
    ordered_delete = models.DateTimeField(auto_now_add=True,null=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
class Address(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=7, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username    
