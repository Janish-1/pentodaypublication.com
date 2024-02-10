from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','email','contact_number','locality','city','zipcode','state']

@admin.register(Product)
class   ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','description','publication','category','product_image1','product_image2','product_image3','product_imagemin1','product_imagemin2','product_imagemin3','product_file']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']

