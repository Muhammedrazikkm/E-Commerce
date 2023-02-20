from django.contrib import admin
from store.models import Products,Category,Offers

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Offers)