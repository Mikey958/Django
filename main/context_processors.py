from . import core_constants
from .models import *

def fcs(request):
    """
    Добавляет в контекст глобальную переменную FCs из модуля core_constants.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        dict: Словарь с ключом 'FCs', содержащий значение core_constants.FCs.
    """
    return {'FCs': core_constants.FCs}

def academic_group(request):
    """
    Добавляет в контекст глобальную переменную ACADEMIC_GROUP из модуля core_constants.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        dict: Словарь с ключом 'ACADEMIC_GROUP', содержащий значение core_constants.ACADEMIC_GROUP.
    """
    return {'ACADEMIC_GROUP': core_constants.ACADEMIC_GROUP}

def get_main_page(request):
    """
    Получает данные для главной страницы сайта.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        QuerySet: Набор объектов MainPage, предварительно загружая связанные изображения.
    """
    return MainPage.objects.prefetch_related('additional_images').all()

def get_skills_page(request):
    """
    Получает данные для страницы навыков.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        QuerySet: Набор всех объектов модели SkillsSet.
    """
    return SkillsSet.objects.all()

def profession_name(request):
    """
    Добавляет в контекст название профессии из модуля core_constants.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        dict: Словарь с ключом 'PROFESSION_NAME', содержащий значение core_constants.PROFESSION_NAME.
    """
    return {'PROFESSION_NAME': core_constants.PROFESSION_NAME}

def site_name(request):
    """
    Добавляет в контекст название сайта из модуля core_constants.

    Параметры:
        request (HttpRequest): HTTP-запрос.

    Возвращает:
        dict: Словарь с ключом 'SITE_NAME', содержащий значение core_constants.SITE_NAME.
    """
    return {'SITE_NAME': core_constants.SITE_NAME}
