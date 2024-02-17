from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chattishgarh','Chattishgarh'),
  ('Dadar Nagar & Haveli','Dadar Nagar & Haveli'),
  ('Daman & diu','Daman & Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Himachal Pradesh','Himanchal Pradesh'),
  ('Gujrat','Gujrat'),
  ('Rajasthan','Rajasthan'),
  ('Punjab','Punjab'),
  ('Uttrakhand','Uttrakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('Haryana','Haryana'),
  ('Karnataka','karnataka'),
  ('Jharkhand','Jharkhand'),
  ('Kerala','Kearala'),
  ('Lakshadweep','Lakshadweep'),
  ('Manipur','Manipur'),
  ('Mizoram','Mizoram'),
  ('Meghalaya','Meghalaya'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Sikkim','Sikkim'),
  ('Tripura','Tripura'),
  ('Telangana','Telangana'),
  ('Tamilnadu','Tamilnadu'),
  ('West Bengal','West Bengal'),
)
class Customer(models.Model):
 user=models.ForeignKey(User, on_delete=models.CASCADE)
 name=models.CharField(max_length=200)
 locality=models.CharField(max_length=200)
 city=models.CharField(max_length=50)
 zipcode=models.IntegerField()
 state =models.CharField(choices=STATE_CHOICES,max_length=50)

 def __str__(self):
  return str(self.id)
 
CATEGORY_CHOICES= (
  ('m', 'mobiles'),
  ('T','Trending deals'),
  ('TW','Top Wear'),
  ('BW','Bottom Wear')
 )

class Product(models.Model):
 title =models.CharField(max_length=100)
 selling_price =models.FloatField()
 discounted_price =models.FloatField()
 description=models.TextField()
 brand=models.CharField(max_length=100)
 category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
 Product_images = models.ImageField(upload_to='media/img/')

 def __str__(self):
  return str(self.id)

class Cart (models.Model):
 user =models.ForeignKey(User, on_delete=models.CASCADE)
 Product =models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity =models.PositiveIntegerField(default=1)

 def __str__(self):
  return str(self.id)
 
STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 Product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Pending')



 




