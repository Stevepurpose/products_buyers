from django.db import models


# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True, null=False, default='undisclosed')
    productname = models.CharField(max_length=255)
    productNumber = models.IntegerField(max_length=None)
    price = models.FloatField()
    production_date = models.DateField(max_length=255)
    expiry_date = models.DateField(max_length=255)

    def __str__(self):
       return f"{self.productname}"
    
class Buyer(models.Model):
      buyername = models.CharField(max_length=255)
      productID = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, default='undisclosed')
      units=models.IntegerField(max_length=None)
      location = models.CharField(max_length=255)

      def __str__(self):
       return f"{self.buyername}"


