# Generated by Django 5.0.3 on 2024-03-25 20:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_category_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_active',
        ),
        migrations.AddField(
            model_name='blog',
            name='aktif',
            field=models.BooleanField(default=False, verbose_name='Yayında mı?'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=50, verbose_name='Fotoğraf'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_home',
            field=models.BooleanField(default=False, verbose_name='Anasayfada mı?'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
    ]
