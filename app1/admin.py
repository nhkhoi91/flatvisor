from django.contrib import admin
from .models import Flat
from .models import Customer
# Register your models here.

admin.site.register(Flat)
admin.site.register(Customer)
