from django.db import models
import uuid


# Create your models here.
class ProductModel(models.Model):
    pid = models.CharField(max_length=255, unique=True)  # Unique identifier, required
    name = models.CharField(
        max_length=100, blank=False
    )  # Required field, cannot be blank
    slug = models.SlugField(unique=True)  # Required field, slug should be unique
    description = models.TextField(
        blank=True, null=True
    )  # Optional field, can be blank or null
    is_digital = models.BooleanField(default=False)  # Defaults to False, required field
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False
    )  # Automatically set on creation
    updated_at = models.DateTimeField(
        auto_now=True, editable=False
    )  # Automatically set on update
    is_active = models.BooleanField(default=True)  # Defaults to True, required field

    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDERED = "BO"
    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out of Stock",
        BACKORDERED: "Back Ordered",
    }
    stock_status = models.CharField(
        max_length=3,
        choices=STOCK_STATUS.items(),  # Use items() to get (value, label) pairs
        default=OUT_OF_STOCK,
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    category=models.ForeignKey('CategoryModel',on_delete=models.SET_NULL,null=True)
    seasonal_event=models.ForeignKey('SeasonalEventModel',on_delete=models.SET_NULL,null=True)


class ProductLineModel(models.Model):
    price = models.DecimalField()
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField()
    weight = models.FloatField()
    product=models.ForeignKey(ProductModel,on_delete=models.PROTECT)


class ProductImageModel(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField()
    order = models.IntegerField()
    product_line=models.ForeignKey(ProductLineModel,on_delete=models.CASCADE)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    parent=models.ForeignKey('self',on_delete=models.PROTECT)


class SeasonalEventModel(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)
