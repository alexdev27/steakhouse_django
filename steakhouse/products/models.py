from django.db.models import Model, CharField, BooleanField, \
    FloatField, TextField, PositiveBigIntegerField, ImageField

# Create your models here.


class Product(Model):
    title = CharField(max_length=150)
    img = ImageField(max_length=100)
    price = PositiveBigIntegerField()
    product_code = CharField(max_length=30)
    weight = FloatField()
    unit = CharField(max_length=30)
    description = TextField()
    status = BooleanField()
    cook_sign = CharField(max_length=30)
    tax_rate = FloatField()
