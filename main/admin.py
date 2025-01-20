from django.contrib import admin
from .models import MainPage, MainPageImage, Demand, Geography, SkillsSet, StatisticSet


class MainPageImageInline(admin.TabularInline):
    """
        Встроенная таблица для управления изображениями, связанными с моделью MainPage.

        Attributes:
            model (Model): Модель, связанная с таблицей изображений (MainPageImage).
            extra (int): Количество пустых строк для добавления новых записей (по умолчанию 1).
    """
    model = MainPageImage
    extra = 1


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    """
       Конфигурация административного интерфейса для модели MainPage.

       Attributes:
           inlines (list): Список встроенных таблиц, связанных с этой моделью.
    """
    inlines = [MainPageImageInline]

# Регистрация остальных моделей в административной панели.
admin.site.register(Demand)
admin.site.register(Geography)
admin.site.register(SkillsSet)
admin.site.register(StatisticSet)
