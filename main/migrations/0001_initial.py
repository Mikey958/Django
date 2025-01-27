# Generated by Django 5.1.4 on 2025-01-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph_salary_level',
                 models.ImageField(upload_to='images/', verbose_name='График уровня зарплат по годам')),
                ('graph_num_vacancy',
                 models.ImageField(upload_to='images/', verbose_name='График количества вакансий по годам')),
                ('salary_table', models.TextField(verbose_name='Таблица уровня зарплат по годам')),
                ('vacancy_table', models.TextField(verbose_name='Таблица количества вакансий по годам')),
            ],
        ),
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graph_salary_level_by_city',
                 models.ImageField(upload_to='images/', verbose_name='График уровень зарплат по городам')),
                ('graph_vacancy_fraction_by_city',
                 models.ImageField(upload_to='images/', verbose_name='График доля вакансий по городам')),
                ('level_by_city_table', models.TextField(verbose_name='Таблица уровень зарплат по городам')),
                ('fraction_by_city_table', models.TextField(verbose_name='Таблица доля вакансий по городам')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Название профессии')),
                ('description', models.TextField(blank=True, verbose_name='Описание профессии')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.TextField(max_length=30, verbose_name='Название таблицы')),
                ('table', models.TextField(verbose_name='Таблица')),
                ('graph_skills', models.ImageField(upload_to='images/', verbose_name='График по скиллам')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='StatisticSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearly_salary_graph',
                 models.ImageField(upload_to='images/', verbose_name='График уровня зарплат по годам')),
                ('yearly_salary_table', models.TextField(verbose_name='Таблица уровня зарплат по годам')),
                ('yearly_vacancy_count_graph',
                 models.ImageField(upload_to='images/', verbose_name='График количества вакансий по годам')),
                ('yearly_vacancy_count_table', models.TextField(verbose_name='Таблица количества вакансий по годам')),
                ('city_salary_graph',
                 models.ImageField(upload_to='images/', verbose_name='График уровня зарплат по городам')),
                ('city_salary_table', models.TextField(verbose_name='Таблица уровня зарплат по городам')),
                ('city_rate_vacancy_graph',
                 models.ImageField(upload_to='images/', verbose_name='График доли вакансий по городам')),
                ('city_rate_vacancy_table', models.TextField(verbose_name='Таблица доли вакансий по городам')),
                ('top20_skills_graph',
                 models.ImageField(upload_to='images/', verbose_name='График топ 20 навыков по годам')),
                ('top20_skills_table', models.TextField(verbose_name='Таблица топ 20 навыков по годам')),
            ],
        ),
    ]
