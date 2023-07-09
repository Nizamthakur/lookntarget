from django.db import models

# Create your models here.
class blog (models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    image = models.ImageField( upload_to="blog_images", blank =True , null = True )
    body  = models.TextField(max_length= 200)
    created_on = models.DateTimeField( auto_now_add=True )
    updated_on = models.DateTimeField( auto_now_add=True)

    class Meta:
        db_table ='userBlog'
        ordering = ("id",)
        verbose_name_plural = 'blog'
    
    def __str__(self):
        return self.title
        
#employee list model 
class Employee(models.Model):
    img = models.ImageField(upload_to="emp_image")
    name = models.CharField(max_length=50)
    words = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"
        ordering = ('id',)
        verbose_name_plural = 'office employee'


    
    



