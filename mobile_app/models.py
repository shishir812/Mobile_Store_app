from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.

class Mobile(models.Model):
    brand_name = models.CharField(max_length=36, null=True)
    model = models.CharField(max_length=12, null=True)
    color = models.CharField(max_length=12, null=True)
    jan_code = models.ImageField(upload_to='images', blank=True)
    image = models.ImageField(upload_to='mobile_pics', blank=True)
    country_id = models.CharField(max_length=1, null=True)
    manufacturer_id = models.CharField(max_length=6, null=True)
    number_id = models.CharField(max_length=5, null=True)


    def __str__(self):
        return self.brand_name


    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.country_id}{self.manufacturer_id}{self.number_id}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.jan_code.save('jan_code.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


