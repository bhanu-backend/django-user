from django.db import models




choices=(
    ('AC','AC'),
    ('TV','TV'),
    ('Refrigerator','Refrigerator'),
    ('Mobile','Mobile'),
    ('Laptop','Laptop'),
    ('Microwave','Microwave'),
    ('Accessories','Accessories'),
)


class Product (models.Model):
    category = models.CharField(max_length=25,choices=choices)
    image = models.ImageField(upload_to="assests/images")
    name = models.CharField(max_length=25)
    description = models.TextField()
    rating = models.SmallIntegerField()
    price = models.FloatField()
    expected_delivery = models.DateTimeField()
     