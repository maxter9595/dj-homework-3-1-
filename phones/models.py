from django.db import models
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        validators=[MinValueValidator(0)]
    )
    image = models.ImageField(
        null=False,
        upload_to='phone_images/'
    )
    release_date = models.DateField(
        null=False
    )
    lte_exists = models.BooleanField(
        null=False
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
