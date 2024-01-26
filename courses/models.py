from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args, kwargs)

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="", blank=True, editable=False, null=False, unique=True, db_index=True)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)
        # Slug bilgisini title bilgisi uzerinden otomatik olarak olusturma talimati verdik.

    def __str__(self):
        return f"{self.title} {self.date}"
    
