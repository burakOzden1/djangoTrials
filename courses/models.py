from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=50)

    def __str__(self):
        return f"{self.name}"
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(args, kwargs)

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images", default="")
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, unique=True, db_index=True)
    # category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, related_name="kurslar") # asagida many to many iliskisi kurdugumuz icin bu satiri sildik.
    categories = models.ManyToManyField(Category)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(args, kwargs)
        # Slug bilgisini title bilgisi uzerinden otomatik olarak olusturma talimati verdik.
        # admin py icinden ayarladik (alternatif olarak iki yontemden birini kullanabilirsin.)

    def __str__(self):
        return f"{self.title} {self.date}"
    

class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")