# Generated by Django 5.0.3 on 2024-03-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blog.category', verbose_name='Kategori'),
        ),
    ]
