from django.db import models


class ConsoleCategory(models.Model):
    console_category_name = models.CharField(max_length=255)
    console_category_image = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.console_category_name


class ManufacturerCategory(models.Model):
    manufacturer_name = models.CharField(max_length=255)
    manufacturer_description = models.CharField(max_length=999)
    manufacturer_logo = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return self.manufacturer_name


class Console(models.Model):
    console_name = models.CharField(max_length=255)
    console_category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE)
    console_manufacturer = models.ForeignKey(ManufacturerCategory, on_delete=models.CASCADE)
    console_short_description = models.CharField(max_length=255)
    console_long_description = models.CharField(max_length=999)
    console_price = models.FloatField()

    def __str__(self):
        return self.console_name


class ConsoleImage(models.Model):
    console_image_image = models.CharField(max_length=999)
    console_image_console = models.ForeignKey(Console, on_delete=models.CASCADE)
