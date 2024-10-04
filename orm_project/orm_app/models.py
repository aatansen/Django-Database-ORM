from django.db import models
import uuid


# Create your models here.
class product_model(models.Model):
    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    is_digital = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField()


class product_line_model(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField()
    is_active = models.BooleanField()
    order = models.IntegerField()
    weight = models.FloatField()


class product_image_model(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()


class category_model(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    is_active = models.BooleanField()


class seasonal_event_model(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)
