# Generated by Django 5.1.4 on 2025-01-03 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Дополнительное изображение')),
                ('main_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_images', to='main.mainpage', verbose_name='Основная страница')),
            ],
        ),
    ]
