from datetime import date

from django.db import models
from django.utils.timezone import now


# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=50, default="product")
    creator = models.ForeignKey("auth.User", default=1)
    category = models.CharField(max_length=100, default='software')
    main_image = models.ImageField(upload_to="Products/", null=True)
    screenshot2 = models.ImageField(upload_to="products/", null=True, )
    screenshot3 = models.ImageField(upload_to="products/", null=True)
    created = models.DateField(default=now, null=True)
    updated = models.DateField(default=now, null=True)
    actual_price = models.IntegerField(default=2000)
    quantity = models.IntegerField(default=5)
    product_file = models.FileField(upload_to="doc_files", null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.p_name


class Giveaway(models.Model):
    g_name = models.CharField(max_length=55, blank=False, null=False, default="my giveaway")
    user = models.ForeignKey("auth.User", default=1)
    p_name = models.ForeignKey("Product", default=1)
    entries = models.IntegerField(default=5)
    created = models.DateField(default=now)
    updated = models.DateField(default=now)
    image = models.ImageField(upload_to="giveaways/Img/", null=True)
    description = models.TextField(blank=False, null=False, default="No description avaiable")
    ending_time = models.DateField(default=now)
    comments = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.g_name


class GiveawayEntry(models.Model):
    user = models.PositiveIntegerField("auth.User", default=1)
    giveaway = models.PositiveIntegerField("Giveaway", default=1)
    created_on = models.DateField(default=now)
    updated = models.DateField(default=now)
    total_points = models.IntegerField(default=0)
    facebook_share_count = models.IntegerField(default=0)
    twitter_share_count = models.IntegerField(default=0)
    google_plus_share_count = models.IntegerField(default=0)
    stumble_share_count = models.IntegerField(default=0)
    linked_share_count = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)
