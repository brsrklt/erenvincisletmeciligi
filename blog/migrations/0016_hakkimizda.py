# Generated by Django 5.0.3 on 2024-03-30 09:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_makinelerimiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hakkimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Başllık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Hakkımızda yazısı')),
                ('image', models.ImageField(upload_to='blogs', verbose_name='Resim')),
                ('mis_viz', ckeditor.fields.RichTextField(verbose_name='Misyon & Vizyon')),
            ],
        ),
    ]
