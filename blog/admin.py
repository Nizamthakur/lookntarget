from django.contrib import admin
from .models import blog, Employee
# Register your models here.
@admin.register(blog)
class BlogPost (admin.ModelAdmin):
    list_display  = ( 'title', 'author', 'created_on',)


@admin.register(Employee)  
class emplye_post(admin.ModelAdmin):
    list_display  = ( 'name',)
        