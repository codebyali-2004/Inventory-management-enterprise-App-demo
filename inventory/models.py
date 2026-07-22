from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_code=models.CharField(max_length=10,
                                  unique=True,
                                  blank=True,
                                  editable=False)
    category=models.CharField(max_length=100)
    quantity=models.PositiveBigIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    gst=models.DecimalField(max_digits=5,decimal_places=2,default=18.00)
    image=models.ImageField(upload_to="products/")



    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        if not self.product_code:
            last_product = Product.objects.order_by('id').last()
            if last_product:
                last_id = int(last_product.product_code[1:])
                self.product_code = f'P{last_id + 1:03d}'
            else:
                self.product_code = 'P001'
        super().save(*args, **kwargs)

# Create your models here.
