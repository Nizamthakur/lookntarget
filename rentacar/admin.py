from django.contrib import admin
from .models import car , car_price, faq
# Register your models here.
@admin.register(car)
class car_info  (admin.ModelAdmin):
    list_display  = ( 'pickup', 'destination', 'Date',)

@admin.register(car_price)
class car_price_info  (admin.ModelAdmin):
    list_display  = ( 'price', 'description',)
@admin.register(faq)
class faq  (admin.ModelAdmin):
    list_display  = ('question',)