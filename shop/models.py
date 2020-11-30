from django.db import models

# Create your models here.


class Product(models.Model):
    prod_id = models.AutoField
    prod_image = models.ImageField(upload_to="shop/images", default="")
    prod_name = models.CharField(max_length=51)
    prod_desc = models.CharField(max_length=511)
    prod_category = models.CharField(max_length=51, default="")
    prod_sub_category = models.CharField(max_length=51, default="")
    prod_price = models.IntegerField(default=0)
    prod_pub_date = models.DateField()

    def __str__(self):
        return self.prod_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=51)
    email = models.CharField(max_length=51)
    phone = models.CharField(max_length=51, default="")
    desc = models.CharField(max_length=511, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5111)
    name = models.CharField(max_length=51)
    email = models.CharField(max_length=51)
    phone = models.CharField(max_length=51)
    address = models.CharField(max_length=511)
    city = models.CharField(max_length=51)
    state = models.CharField(max_length=51)
    zip_code = models.CharField(max_length=51)

