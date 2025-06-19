from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
class ProductList(models.Model):
    title = models.CharField(max_length = 255, unique=True,db_index = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, db_index = True)
    featured = models.BooleanField(db_index = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default=None, related_name='category_name')
    
    def __str__(self) -> str:
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produclist = models.ForeignKey(ProductList, on_delete= models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places=2)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    
    class Meta:
        unique_together = ('produclist', 'user')
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name ="delivery_crew", null=True)
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    produclist = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('order', 'produclist')