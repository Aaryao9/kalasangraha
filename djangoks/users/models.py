from django.db import models
from django.utils.text import slugify



# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True) 
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    sold = models.IntegerField()
    stock = models.IntegerField()
    seller = models.CharField(max_length=255)
    listedin = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    

class Cart(models.Model):
        user= models.OneToOneField(User, on_delete=models.CASCADE) 
    
    
def __str__(self):
        return self.name


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    addedon = models.DateTimeField(auto_now_add=True, blank=True, null=True)   
    def __str__(self):
        return self.name    
    
    

    
    



class Order(models.Model):  
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total = models.DecimalField(max_digits=5, decimal_places=2)
    orderedon = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
class OrderItems(models.Model):
    order_id= models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
    
    def total_price(self):
        return self.price * self.quantity