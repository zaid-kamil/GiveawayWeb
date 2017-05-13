from datetime import date

from django.db import models
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey("auth.User")
    category = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="Products/", null=True)
    screenshot2 = models.ImageField(upload_to="products/", null=True)
    screenshot3 = models.ImageField(upload_to="products/", null=True)

    created = models.DateField(default=now)
    updated = models.DateField(default=now)
    actual_price = models.IntegerField()
    quantity = models.IntegerField()
    product_file = models.FileField(upload_to="doc_files", null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Giveaway(models.Model):
    name = models.CharField(max_length=55,blank=False, null=False)
    user = models.ForeignKey("auth.User")
    product_name = models.ForeignKey("Product")
    entries = models.IntegerField()
    created = models.DateField(default=now)
    updated = models.DateField(default=now)
    image = models.ImageField(upload_to="giveaways/Img/", null=True)

    description = models.TextField( blank=False, null=False)
    prize = models.IntegerField()
    ending_time = models.DateField(default=now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Entry(models.Model):
    user_name = models.ForeignKey("auth.User")
    giveaway = models.ForeignKey("Giveaway")
    facebook_share = models.TextField(blank=True, null=True)
    twitter_share = models.TextField(blank=True, null=True)
    google_plus_share = models.TextField(blank=True, null=True)
    created_on = models.DateField(default=now)
    updated = models.DateField(default=now)
    total_points = models.IntegerField()
    facebook_share_count = models.IntegerField(default=0)
    twitter_share_count = models.IntegerField(default=0)
    google_plus_share_count = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)
