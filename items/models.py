from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30, default="")
    category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    pub_name = models.CharField(max_length=30, default="")
    image = models.ImageField(upload_to='items/image', default="")

    def __str__(self):
        return self.product_name
