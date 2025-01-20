from django.db import models


class MainPage(models.Model):
    """
       Модель для главной страницы сайта.

       Поля:
           title (TextField): Название профессии. Может быть пустым.
           description (TextField): Описание профессии. Может быть пустым.
           image (ImageField): Основное изображение профессии. Обязательно для заполнения.
    """
    title = models.TextField(blank=True, verbose_name='Название профессии')
    description = models.TextField(blank=True, verbose_name='Описание профессии')
    image = models.ImageField(blank=False, verbose_name='Изображение', upload_to='images/')


class MainPageImage(models.Model):
    """
       Модель для дополнительных изображений на главной странице.

       Поля:
           main_page (ForeignKey): Ссылка на модель MainPage. При удалении записи MainPage связанные изображения удаляются.
           image (ImageField): Дополнительное изображение. Обязательно для заполнения.
    """
    main_page = models.ForeignKey(MainPage, on_delete=models.CASCADE, related_name='additional_images',
                                  verbose_name='Основная страница')
    image = models.ImageField(verbose_name='Дополнительное изображение', upload_to='images/')


class Demand(models.Model):
    """
       Модель для хранения данных о спросе на профессию.

       Поля:
           graph_salary_level (ImageField): График уровня зарплат по годам.
           graph_num_vacancy (ImageField): График количества вакансий по годам.
           salary_table (TextField): Таблица уровня зарплат по годам.
           vacancy_table (TextField): Таблица количества вакансий по годам.
    """
    graph_salary_level = models.ImageField(blank=False,
                                           verbose_name='График уровня зарплат по годам')
    graph_num_vacancy = models.ImageField(blank=False,
                                          verbose_name='График количества вакансий по годам')
    salary_table = models.TextField(blank=False, verbose_name='Таблица уровня зарплат по годам')
    vacancy_table = models.TextField(blank=False, verbose_name='Таблица количества вакансий по годам')


class Geography(models.Model):
    """
       Модель для хранения данных о географическом распределении вакансий.

       Поля:
           graph_salary_level_by_city (ImageField): График уровня зарплат по городам.
           graph_vacancy_fraction_by_city (ImageField): График доли вакансий по городам.
           level_by_city_table (TextField): Таблица уровня зарплат по городам.
           fraction_by_city_table (TextField): Таблица доли вакансий по городам.
    """
    graph_salary_level_by_city = models.ImageField(blank=False,
                                                   verbose_name='График уровень зарплат по городам')
    graph_vacancy_fraction_by_city = models.ImageField(blank=False,
                                                       verbose_name='График доля вакансий по городам')
    level_by_city_table = models.TextField(blank=False, verbose_name='Таблица уровень зарплат по городам')
    fraction_by_city_table = models.TextField(blank=False, verbose_name='Таблица доля вакансий по городам')


class SkillsSet(models.Model):
    """
        Модель для хранения данных о навыках.

        Поля:
            table_name (TextField): Название таблицы. Максимум 30 символов.
            table (TextField): Данные таблицы навыков.
            graph_skills (ImageField): График по навыкам.
    """
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    table = models.TextField(blank=False, verbose_name='Таблица')
    graph_skills = models.ImageField(blank=False, verbose_name='График по скиллам')

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'


class StatisticSet(models.Model):
    """
        Модель для хранения полной статистики по профессии.

        Поля:
            yearly_salary_graph (ImageField): График уровня зарплат по годам.
            yearly_salary_table (TextField): Таблица уровня зарплат по годам.
            yearly_vacancy_count_graph (ImageField): График количества вакансий по годам.
            yearly_vacancy_count_table (TextField): Таблица количества вакансий по годам.
            city_salary_graph (ImageField): График уровня зарплат по городам.
            city_salary_table (TextField): Таблица уровня зарплат по городам.
            city_rate_vacancy_graph (ImageField): График доли вакансий по городам.
            city_rate_vacancy_table (TextField): Таблица доли вакансий по городам.
            top20_skills_graph (ImageField): График топ-20 навыков по годам.
            top20_skills_table (TextField): Таблица топ-20 навыков по годам.
    """
    yearly_salary_graph = models.ImageField(blank=False, verbose_name='График уровня зарплат по годам')
    yearly_salary_table = models.TextField(blank=False, verbose_name='Таблица уровня зарплат по годам')

    yearly_vacancy_count_graph = models.ImageField(blank=False, verbose_name='График количества вакансий по годам')
    yearly_vacancy_count_table = models.TextField(blank=False, verbose_name='Таблица количества вакансий по годам')

    city_salary_graph = models.ImageField(blank=False, verbose_name='График уровня зарплат по городам')
    city_salary_table = models.TextField(blank=False, verbose_name='Таблица уровня зарплат по городам')

    city_rate_vacancy_graph = models.ImageField(blank=False, verbose_name='График доли вакансий по городам')
    city_rate_vacancy_table = models.TextField(blank=False, verbose_name='Таблица доли вакансий по городам')

    top20_skills_graph = models.ImageField(blank=False, verbose_name='График топ 20 навыков по годам')
    top20_skills_table = models.TextField(blank=False, verbose_name='Таблица топ 20 навыков по годам')
