# Generated by Django 5.0.3 on 2024-03-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_home',
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category', verbose_name='Kategori'),
        ),
    ]
