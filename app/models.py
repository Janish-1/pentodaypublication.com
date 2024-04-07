from django.db import models
from django.contrib.auth.models import User
from django .core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
STATE_CHOICES=(
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Arunachal Pradesh' , 'Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhatisgarh','Chhatisgarh'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh')
)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=True)
    contact_number = models.CharField(max_length=200,null=True,blank=True)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    def __str__(self):
      return str(self.id)
CATEGORY_CHOICES=(
    ('Ram','Ram se Ram Tak'),
    ('Paas','Paas Jab Se Tum Nahi'),
    ('Hind','Hind Ki Awaz'),
    ('Ek','Ek Radha Geet Gati Hai'),
   
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    discounted_price = models.FloatField()
    description = models.TextField()
    publication = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image1 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_image2 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_image3 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_imagemin1 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_imagemin2 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_imagemin3 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_imagemin4 = models.ImageField(upload_to='productimg',null=True,blank=True)
    product_file = models.FileField(upload_to="productfile",null=True,blank=True)
  
    def __str__(self):
     return str(self.id)
    
class Cart(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)
   def __str__(self):
      return str(self.id)
   @property
   def total_cost(self):
      return self.quantity*self.product.discounted_price
   
STATUS_CHOICES=(
   ('Accepted','Accepted'),
   ('Packed','Packed'),
   ('On the way','On the way'),
   ('Delivered','Delivered'),
   ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)
   ordered_date = models.DateTimeField(auto_now_add=True)
   status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

   @property
   def total_cost(self):
      return self.quantity*self.product.discounted_price