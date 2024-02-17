from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced



@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display =['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display =['id','title','selling_price','discounted_price','description',
 'brand','category','Product_images']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
 list_display =['id','user','Product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedtModelAdmin(admin.ModelAdmin):
 list_display =['id','user','customer','Product','quantity','ordered_date','status']



# Register your models here.
