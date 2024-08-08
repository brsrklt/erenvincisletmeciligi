from django.db import models
from django.utils.text import slugify

# Create your models here.
from ckeditor.fields import RichTextField

class Makinelerimiz(models.Model):
    title = models.CharField(max_length = 200,verbose_name="Makine adı")
    image = models.ImageField(upload_to="blogs", verbose_name="Resim")
    description = RichTextField(verbose_name="Açıklama")
    is_active = models.BooleanField(verbose_name="Yayında mı?")
    slug = models.SlugField(blank=True, unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.title
    

class Hakkimizda(models.Model):
    title = models.CharField(verbose_name="Başllık",max_length=300)
    content = RichTextField(verbose_name="Hakkımızda yazısı")
    image = models.ImageField(upload_to="blogs", verbose_name="Resim")
    mis_viz = RichTextField(verbose_name="Misyon & Vizyon")



    def __str__(self):
        return self.title

class İletisim(models.Model):
    Ad_1 = models.CharField(verbose_name="1.Kişi Adı", max_length=200)
    tel_1 = models.CharField(verbose_name="1.Kişi Telefon", max_length=200)

    Ad_2 = models.CharField(verbose_name="2.Kişi Adı", max_length=200)
    tel_2 = models.CharField(verbose_name="2.Kişi Telefon", max_length=200)

    adres = models.CharField(verbose_name="Açık adres", max_length=200)

    mail = models.CharField(verbose_name="mail", max_length=200, blank=True)

    def __str__(self):
        return self.Ad_1





class Category(models.Model):
    name =models.CharField(max_length=150)
    slug = models.SlugField(null=True,blank=True, unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length = 200,verbose_name="Başlık")
    image = models.ImageField(upload_to="blogs", verbose_name="Resim")
    description = RichTextField(verbose_name="İçerik")
    is_active = models.BooleanField(verbose_name="Yayında mı?")
    slug = models.SlugField(blank=True, unique=True,db_index=True,editable=False)
    categories = models.ManyToManyField(Category, blank=True, verbose_name = "Kategori")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    



