from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    
    def __str__(self):
        return self.product_name

    @property
    def offer_price(self):
        offs=Offers.objects.filter(product=self)
        if offs:
            off=offs[0]
            offer_price=self.price - off.discount
            return offer_price
        else:   
            return self.price

    @property
    def reviews(self):
        qs=Reviews.objects.filter(products=self)
        return qs
    @property
    def avg(self):
        qs=self.reviews
        if qs:
            total=sum([r.rating for r in qs])
            return total/len(qs)
        else:
            return 0

class Carts(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order_placed","order_placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    qty=models.PositiveIntegerField(default=1)

class Order(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    curDate=datetime.date.today()
    expDate=curDate+datetime.timedelta(days=5)
    expected_delivery_date=models.DateField(default=expDate)
    address=models.CharField(max_length=200,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment

class Offers(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    discount=models.PositiveIntegerField(default=0)
    isAvailable=models.BooleanField(default=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)

