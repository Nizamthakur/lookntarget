from django.db import models

# Create your models here.
class car (models.Model):
    pickup= models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    image = models.ImageField( upload_to="blog_images", blank =True , null = True )
    Date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_on = models.DateTimeField( auto_now_add=True )
    updated_on = models.DateTimeField( auto_now_add=True)

    class Meta:
        db_table ='carRequest'
        ordering = ("-id",)
        verbose_name_plural = 'Car Request'
    
    def __str__(self):
        return self.pickup

# carprice model 
class car_price (models.Model):
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
        
    
    class Meta:
        db_table ='carprice'
        ordering = ("id",)
        verbose_name_plural = ("car price")
    
    def __str__(self):
        return self.price 
# FAQ
class faq (models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=300)
    

    class Meta:
        db_table ='faq'
        ordering = ("id",)
        verbose_name_plural = ("FAQ")
    
    def __str__(self):
        return self.question
    
