from django.contrib import admin

# Register your models here.
from stripe_api.models import Item, Order

admin.site.register(Item)
admin.site.register(Order)