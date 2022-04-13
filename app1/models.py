from email.policy import default
from django.db import models


# Create your models here.

# class Owner(models.Model):
#     owner_id = models.AutoField(primary_key=True,default="")
#     owner_email = models.CharField(max_length=50)
#     owner_password = models.CharField(max_length=10)
    
    

#     class Meta:
#         db_table = "owner"

class Medicine(models.Model):
    
    medicine_name = models.CharField(max_length=50)
    medicine_quantity = models.CharField(max_length=100)
    medicine_price = models.CharField(max_length=100)
    purchace_price = models.CharField(max_length=100,default=0)
    selling_cost = models.CharField(max_length=100,default=0)
    medicine_image = models.ImageField(upload_to = 'medicine/')
    
   

    class Meta:
        db_table = "medicine"


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_email = models.CharField(max_length=50)
    owner_password = models.CharField(max_length=10)

    class Meta:
        db_table = "owner"

class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = 'bill'

