from django.db import models

class Item(models.Model):
    item_slug = models.AutoField
    item_title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    item_description = models.CharField(max_length=2000)
    item_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.item_title
