from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        if self.slug:  # Check if the slug exists
            return f"{self.name} - {self.slug}"
        else:
            return self.name  # Return the name if slug is empty

    def get_absolute_url(self):
        return reverse("list-category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='un-branded')
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/', )
    price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        if self.slug:  # Check if the slug exists
            return f"{self.title} - {self.slug}"
        else:
            return self.title  # Return the title if slug is empty

    def get_absolute_url(self):
        return reverse("product-info", args=[self.slug])
