<div align="center">
<h1>Django Database ORM</h1>
</div>

## Context
- [Preparation](#preparation)
- [Django Model](#django-model)
    - [Building Multiple Models](#building-multiple-models)
    - [DateTimeField Options](#datetimefield-options)

### Preparation
- Create project 
    - `django-admin startproject orm_project`
- Create app 
    - `cd orm_project`
    - `py manage.py startapp orm_app`
- Add app in `INSTALLED_APPS`
    ```py
    INSTALLED_APPS = [
        ...
        'orm_app',
    ]
    ```

[⬆️ Go to top](#context)

### Django Model
#### Building Multiple Models
- [Django Model Field Reference](https://docs.djangoproject.com/en/5.1/ref/models/fields/)
- Open `models.py` in app directory and create model
    ```py
    from django.db import models
    import uuid

    # Create your models here.
    class product_model(models.Model):
        pid=models.CharField(max_length=255)
        name=models.CharField(max_length=100)
        slug=models.SlugField()
        description=models.TextField()
        is_digital=models.BooleanField()
        created_at=models.DateTimeField()
        is_active=models.BooleanField()

    class product_line_model(models.Model):
        price=models.DecimalField()
        sku=models.UUIDField(default=uuid.uuid4)
        stock_qty=models.IntegerField()
        is_active=models.BooleanField()
        order=models.IntegerField()
        weight=models.FloatField()

    class product_image_model(models.Model):
        name=models.CharField(max_length=100)
        alternative_text=models.CharField(max_length=100)
        url=models.ImageField()
        order=models.IntegerField()

    class category_model(models.Model):
        name=models.CharField(max_length=100)
        slug=models.SlugField()
        is_active=models.BooleanField()

    class seasonal_event_model(models.Model):
        start_date=models.DateTimeField()
        end_date=models.DateTimeField()
        name=models.CharField(max_length=100)
    ```

[⬆️ Go to top](#context)

#### DateTimeField Options
- In created `auto_now_add` is used
- In updated `auto_now` is used
    ```py
    class product_model(models.Model):
        ...
        created_at=models.DateTimeField(auto_now_add=True,editable=False)
        updated_at=models.DateTimeField(auto_now=True,editable=False)
        ...
    ```
    - `editable=False` is used to prevent appearing in form 

[⬆️ Go to top](#context)
