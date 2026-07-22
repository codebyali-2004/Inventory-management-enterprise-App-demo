from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    quantity=models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to="products/")



    def __str__(self):
        return self.product_name

# Create your models here.
