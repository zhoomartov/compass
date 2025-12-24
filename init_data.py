#!/usr/bin/env python
"""
Скрипт для заполнения базы данных тестовыми данными
Запустить: python init_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'compass.settings')
django.setup()

from site_app.models import Destination, Tour, BlogPost
from django.utils.text import slugify
from datetime import datetime

def create_destinations():
    """Создание направлений"""
    destinations_data = [
        {'name': 'Иссык-Куль', 'country': 'Кыргызстан', 'description': 'Жемчужина Центральной Азии - второе по величине горное озеро в мире. Кристально чистая вода, горные пики и целебный воздух.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': True},
        {'name': 'Ала-Арча', 'country': 'Кыргызстан', 'description': 'Национальный парк в горах Тянь-Шаня. Идеальное место для треккинга и альпинизма с потрясающими видами.', 'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b', 'featured': True},
        {'name': 'Алтай', 'country': 'Россия', 'description': 'Край нетронутой природы с бирюзовыми реками, высокими горами и древними культурами. Место силы и красоты.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': True},
        {'name': 'Гималаи', 'country': 'Непал', 'description': 'Родина Эвереста и буддистских монастырей. Треккинг к базовому лагерю - мечта каждого путешественника.', 'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa', 'featured': True},
        {'name': 'Казбеги', 'country': 'Грузия', 'description': 'Горы Кавказа, древние храмы и знаменитая гора Казбек. Идеально для пеших походов и фотографии.', 'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17', 'featured': True},
        {'name': 'Камчатка', 'country': 'Россия', 'description': 'Земля вулканов, гейзеров и медведей. Один из самых диких и удивительных уголков планеты.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': False},
        {'name': 'Фанские горы', 'country': 'Таджикистан', 'description': 'Кристально чистые озёра и снежные вершины Памира. Рай для треккеров.', 'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba', 'featured': True},
        {'name': 'Патagonia', 'country': 'Аргентина/Чили', 'description': 'Ледники, торосы и грандиозные горы. Классика мирового треккинга.', 'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470', 'featured': True},
        {'name': 'Аннапурна', 'country': 'Непал', 'description': 'Кольцо Аннапурны — один из самых живописных маршрутов в Гималаях.', 'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa', 'featured': False},
        {'name': 'Байкал', 'country': 'Россия', 'description': 'Самое глубокое озеро мира с кристальной водой и уникальной природой.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': True},
        {'name': 'Каракорум', 'country': 'Пакистан', 'description': 'Горы Каракорум с вершинами выше 8000 м. Треккинг к К2.', 'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b', 'featured': False},
        {'name': 'Сванетия', 'country': 'Грузия', 'description': 'Средневековые башни, ледники и горные деревни. Атмосфера древней Грузии.', 'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17', 'featured': True},
        {'name': 'Торрес-дель-Пайне', 'country': 'Чили', 'description': 'Национальный парк с гранитными башнями и бирюзовыми озёрами.', 'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470', 'featured': True},
        {'name': 'Долина Ала-Тоо', 'country': 'Кыргызстан', 'description': 'Снежные пики, альпийские луга и чистейшие реки.', 'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b', 'featured': False},
        {'name': 'Пик Ленина', 'country': 'Кыргызстан/Таджикистан', 'description': 'Классическое восхождение на семитысячник с потрясающими видами.', 'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba', 'featured': False},
        {'name': 'Каппадокия', 'country': 'Турция', 'description': 'Воздушные шары, подземные города и скальные ландшафты.', 'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e', 'featured': True},
        {'name': 'Занскар', 'country': 'Индия', 'description': 'Гималаи Ладакха — один из самых удалённых и красивых регионов.', 'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa', 'featured': False},
        {'name': 'Караколь', 'country': 'Кыргызстан', 'description': 'Город у подножия Тянь-Шаня, ворота в ущелья и озёра.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': False},
        {'name': 'Байкальский хребет', 'country': 'Россия', 'description': 'Дикие тропы вдоль Байкала с видами на озеро.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': False},
        {'name': 'Перуанские Анды', 'country': 'Перу', 'description': 'Дорога к Мачу-Пикчу через тропические леса и горы.', 'image_url': 'https://images.unsplash.com/photo-1519671482749-fd09be7ccbf7', 'featured': True},
        {'name': 'Килиманджаро', 'country': 'Танзания', 'description': 'Восхождение на высочайшую точку Африки.', 'image_url': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05', 'featured': True},
        {'name': 'Долина Шари', 'country': 'Марокко', 'description': 'Оазисы, каньоны и пустыня Сахара в одном месте.', 'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4', 'featured': False},
        {'name': 'Эльбрус', 'country': 'Россия', 'description': 'Высочайшая вершина Европы. Классика альпинизма.', 'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b', 'featured': True},
        {'name': 'Ладакх', 'country': 'Индия', 'description': 'Высокогорная пустыня с буддистскими монастырями.', 'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa', 'featured': False},
        {'name': 'Тянь-Шань', 'country': 'Кыргызстан', 'description': 'Небесные горы с ледниками и альпийскими лугами.', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4', 'featured': True}
    ]

    destinations = []
    for data in destinations_data:
        dest, created = Destination.objects.get_or_create(
            name=data['name'],
            country=data['country'],
            defaults=data
        )
        destinations.append(dest)
        if created:
            print(f'✓ Создано направление: {dest.name}')
    return destinations


def create_tours(destinations):
    """Создание туров"""
    # Создаём словарь для быстрого доступа к направлениям по имени
    dest_dict = {d.name: d for d in destinations}

    # Полный список из 25 туров — по 2 тура на каждое из 25 направлений
    tours_data = [
        # 1. Иссык-Куль
        {
            'title': 'Треккинг вокруг Иссык-Куля',
            'destination': dest_dict.get('Иссык-Куль'),
            'description': 'Незабываемое путешествие вдоль берегов высокогорного озера. Ущелья, культура и потрясающие пейзажи.',
            'duration_days': 7,
            'price': 650.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Гостевые дома\n• Трехразовое питание\n• Гид\n• Трансферы\n• Страховка',
            'itinerary': 'День 1: Бишкек → Иссык-Куль\nДень 2-5: Треккинг\nДень 6: Горячие источники\nДень 7: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Велосипедный тур по Иссык-Кулю',
            'destination': dest_dict.get('Иссык-Куль'),
            'description': 'Активный велотур по побережью озера с посещением древних петроглифов и пляжей.',
            'duration_days': 6,
            'price': 580.00,
            'difficulty': 'easy',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Велосипеды\n• Проживание\n• Питание\n• Гид',
            'itinerary': 'День 1: Прибытие\nДень 2-5: Велотур\nДень 6: Возвращение',
            'available': True,
            'featured': False
        },
        # 2. Ала-Арча
        {
            'title': 'Восхождение в Ала-Арче',
            'destination': dest_dict.get('Ала-Арча'),
            'description': 'Горный тур с восхождением на вершины нацпарка.',
            'duration_days': 5,
            'price': 480.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Снаряжение\n• Лагерь\n• Питание\n• Гид-альпинист',
            'itinerary': 'День 1: Акклиматизация\nДень 2-3: Восхождение\nДень 4: Спуск\nДень 5: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Треккинг по Ала-Арче',
            'destination': dest_dict.get('Ала-Арча'),
            'description': 'Легкий треккинг по ущельям и водопадам парка.',
            'duration_days': 4,
            'price': 350.00,
            'difficulty': 'moderate',
            'max_group_size': 15,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Гид\n• Питание\n• Трансфер',
            'itinerary': 'День 1: Переезд\nДень 2-3: Треккинг\nДень 4: Возвращение',
            'available': True,
            'featured': False
        },
        # 3. Алтай
        {
            'title': 'Золотое кольцо Алтая',
            'destination': dest_dict.get('Алтай'),
            'description': 'Озёра, водопады, петроглифы и встречи с местными.',
            'duration_days': 10,
            'price': 890.00,
            'difficulty': 'moderate',
            'max_group_size': 15,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Эко-кемпинги\n• Полный пансион\n• Транспорт\n• Гид',
            'itinerary': 'День 1-2: Переезд\nДень 3-8: Экскурсии\nДень 9: Свободный\nДень 10: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Рафтинг по Катуни',
            'destination': dest_dict.get('Алтай'),
            'description': 'Сплав по горным рекам Алтая с ночёвками в палатках.',
            'duration_days': 7,
            'price': 720.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Рафт\n• Питание\n• Гид',
            'itinerary': 'День 1-7: Сплав и стоянки',
            'available': True,
            'featured': False
        },
        # 4. Гималаи (Непал)
        {
            'title': 'Базовый лагерь Эвереста',
            'destination': dest_dict.get('Гималаи'),
            'description': 'Легендарный треккинг к Эвересту.',
            'duration_days': 14,
            'price': 1450.00,
            'difficulty': 'hard',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Перелёты\n• Лоджи\n• Портеры\n• Гид',
            'itinerary': 'День 1-2: Катманду\nДень 3-10: Трек\nДень 11-14: Спуск/вылет',
            'available': True,
            'featured': True
        },
        {
            'title': 'Треккинг в долине Лангтанг',
            'destination': dest_dict.get('Гималаи'),
            'description': 'Спокойный маршрут с видами на Гималаи.',
            'duration_days': 8,
            'price': 850.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Лоджи\n• Питание\n• Гид',
            'itinerary': 'День 1-8: Треккинг',
            'available': True,
            'featured': False
        },
        # 5. Казбеги
        {
            'title': 'Винный тур по Грузии',
            'destination': dest_dict.get('Казбеги'),
            'description': 'Дегустации и культура в горах.',
            'duration_days': 8,
            'price': 750.00,
            'difficulty': 'easy',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'includes': '• Отели\n• Дегустации\n• Транспорт',
            'itinerary': 'День 1-2: Тбилиси\nДень 3-5: Кахетия\nДень 6-7: Казбеги\nДень 8: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Треккинг к Гергети',
            'destination': dest_dict.get('Казбеги'),
            'description': 'Пеший поход к знаменитой церкви на фоне горы Казбек.',
            'duration_days': 4,
            'price': 420.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'includes': '• Гид\n• Питание\n• Трансфер',
            'itinerary': 'День 1: Переезд\nДень 2-3: Трек\nДень 4: Возвращение',
            'available': True,
            'featured': False
        },
        # 6. Камчатка
        {
            'title': 'Вулканы Камчатки',
            'destination': dest_dict.get('Камчатка'),
            'description': 'Вулканы, гейзеры и медведи.',
            'duration_days': 12,
            'price': 1680.00,
            'difficulty': 'moderate',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Перелёты\n• Вертолёт\n• Гид',
            'itinerary': 'День 1-2: Петропавловск\nДень 3-10: Вулканы\nДень 11: Гейзеры\nДень 12: Вылет',
            'available': True,
            'featured': True
        },
        {
            'title': 'Пеший тур по Долине гейзеров',
            'destination': dest_dict.get('Камчатка'),
            'description': 'Вертолёт + треккинг в долине гейзеров.',
            'duration_days': 7,
            'price': 1200.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Вертолёт\n• Питание\n• Гид',
            'itinerary': 'День 1-7: Экспедиция',
            'available': True,
            'featured': False
        },
        # 7. Фанские горы
        {
            'title': 'Треккинг по Фанским горам',
            'destination': dest_dict.get('Фанские горы'),
            'description': 'Озёра и пики Памира.',
            'duration_days': 9,
            'price': 720.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba',
            'includes': '• Палатки\n• Питание\n• Гид',
            'itinerary': 'День 1: Душанбе\nДень 2-8: Трек\nДень 9: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Восхождение на пик Фанские',
            'destination': dest_dict.get('Фанские горы'),
            'description': 'Альпинистский тур на вершины.',
            'duration_days': 10,
            'price': 950.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba',
            'includes': '• Снаряжение\n• Гид',
            'itinerary': 'День 1-10: Экспедиция',
            'available': True,
            'featured': False
        },
        # 8. Patagonia
        {
            'title': 'W Trek в Patagonia',
            'destination': dest_dict.get('Патagonia'),
            'description': 'Классика: башни и ледники.',
            'duration_days': 5,
            'price': 980.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470',
            'includes': '• Рефугио\n• Питание',
            'itinerary': 'День 1-5: W-тропа',
            'available': True,
            'featured': True
        },
        {
            'title': 'Torres del Paine O Circuit',
            'destination': dest_dict.get('Патagonia'),
            'description': 'Полный круг вокруг парка.',
            'duration_days': 9,
            'price': 1400.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470',
            'includes': '• Кемпинги\n• Питание',
            'itinerary': 'День 1-9: O-тропа',
            'available': True,
            'featured': False
        },
        # 9. Аннапурна
        {
            'title': 'Кольцо Аннапурны',
            'destination': dest_dict.get('Аннапурна'),
            'description': 'Живописный маршрут Гималаев.',
            'duration_days': 12,
            'price': 1350.00,
            'difficulty': 'hard',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Лоджи\n• Портеры',
            'itinerary': 'День 1-12: Кольцо',
            'available': True,
            'featured': True
        },
        {
            'title': 'Трек к базовому лагерю Аннапурны',
            'destination': dest_dict.get('Аннапурна'),
            'description': 'Короткий тур к лагерю.',
            'duration_days': 10,
            'price': 1100.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Гид\n• Питание',
            'itinerary': 'День 1-10: Трек',
            'available': True,
            'featured': False
        },
        # 10. Байкал
        {
            'title': 'Байкал зимой',
            'destination': dest_dict.get('Байкал'),
            'description': 'Лёд и пещеры Байкала.',
            'duration_days': 6,
            'price': 800.00,
            'difficulty': 'easy',
            'max_group_size': 15,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Гостевые дома\n• Трансферы',
            'itinerary': 'День 1-6: Озеро',
            'available': True,
            'featured': True
        },
        {
            'title': 'Летний треккинг по Байкалу',
            'destination': dest_dict.get('Байкал'),
            'description': 'Пеший тур по берегу.',
            'duration_days': 8,
            'price': 700.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Палатки\n• Питание',
            'itinerary': 'День 1-8: Треккинг',
            'available': True,
            'featured': False
        },
        # 11. Каракорум
        {
            'title': 'Экспедиция в Каракорум',
            'destination': dest_dict.get('Каракорум'),
            'description': 'Трек к K2.',
            'duration_days': 20,
            'price': 4500.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Палатки\n• Портеры',
            'itinerary': 'День 1-20: Экспедиция',
            'available': True,
            'featured': False
        },
        {
            'title': 'Треккинг в долине Бальторо',
            'destination': dest_dict.get('Каракорум'),
            'description': 'Вид на K2 и ледники.',
            'duration_days': 15,
            'price': 3500.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Гид\n• Питание',
            'itinerary': 'День 1-15: Трек',
            'available': True,
            'featured': False
        },
        # 12. Сванетия
        {
            'title': 'Сванетия: Башни и ледники',
            'destination': dest_dict.get('Сванетия'),
            'description': 'Средневековые башни и тропы.',
            'duration_days': 7,
            'price': 680.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'includes': '• Гостевые дома\n• Гид',
            'itinerary': 'День 1: Местиа\nДень 2-6: Трек\nДень 7: Возвращение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Трек к Ушгульскому перевалу',
            'destination': dest_dict.get('Сванетия'),
            'description': 'Перевалы и деревни Сванетии.',
            'duration_days': 8,
            'price': 750.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'includes': '• Питание\n• Гид',
            'itinerary': 'День 1-8: Трек',
            'available': True,
            'featured': False
        },
        # 13. Торрес-дель-Пайне
        {
            'title': 'Треккинг к Торрес-дель-Пайне',
            'destination': dest_dict.get('Торрес-дель-Пайне'),
            'description': 'Гранитные башни и озёра.',
            'duration_days': 6,
            'price': 1100.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470',
            'includes': '• Кемпинги',
            'itinerary': 'День 1-6: Трек',
            'available': True,
            'featured': True
        },
        {
            'title': 'Фототур в Торрес-дель-Пайне',
            'destination': dest_dict.get('Торрес-дель-Пайне'),
            'description': 'Фотосъёмка пейзажей парка.',
            'duration_days': 5,
            'price': 900.00,
            'difficulty': 'easy',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470',
            'includes': '• Гид-фотограф',
            'itinerary': 'День 1-5: Парк',
            'available': True,
            'featured': False
        },
        # 14. Долина Ала-Тоо
        {
            'title': 'Треккинг в Долине Ала-Тоо',
            'destination': dest_dict.get('Долина Ала-Тоо'),
            'description': 'Снежные пики и луга.',
            'duration_days': 6,
            'price': 550.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Палатки\n• Гид',
            'itinerary': 'День 1-6: Трек',
            'available': True,
            'featured': False
        },
        {
            'title': 'Альпинизм в Ала-Тоо',
            'destination': dest_dict.get('Долина Ала-Тоо'),
            'description': 'Восхождения на вершины.',
            'duration_days': 8,
            'price': 800.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Снаряжение',
            'itinerary': 'День 1-8: Экспедиция',
            'available': True,
            'featured': False
        },
        # 15. Пик Ленина
        {
            'title': 'Восхождение на Пик Ленина',
            'destination': dest_dict.get('Пик Ленина'),
            'description': 'Семитысячник Памира.',
            'duration_days': 18,
            'price': 2500.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba',
            'includes': '• Базовый лагерь',
            'itinerary': 'День 1-18: Восхождение',
            'available': True,
            'featured': False
        },
        {
            'title': 'Трек к базовому лагерю Пика Ленина',
            'destination': dest_dict.get('Пик Ленина'),
            'description': 'Треккинг к лагерю без восхождения.',
            'duration_days': 10,
            'price': 1200.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1519681393784-d120267933ba',
            'includes': '• Гид',
            'itinerary': 'День 1-10: Трек',
            'available': True,
            'featured': False
        },
        # 16. Каппадокия
        {
            'title': 'Воздушные шары Каппадокии',
            'destination': dest_dict.get('Каппадокия'),
            'description': 'Полёт на шарах и скальные города.',
            'duration_days': 5,
            'price': 550.00,
            'difficulty': 'easy',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e',
            'includes': '• Отели\n• Полёт',
            'itinerary': 'День 1-5: Каппадокия',
            'available': True,
            'featured': True
        },
        {
            'title': 'Велотур по Каппадокии',
            'destination': dest_dict.get('Каппадокия'),
            'description': 'Велосипеды по долинам.',
            'duration_days': 4,
            'price': 450.00,
            'difficulty': 'easy',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e',
            'includes': '• Велосипеды',
            'itinerary': 'День 1-4: Тур',
            'available': True,
            'featured': False
        },
        # 17. Занскар
        {
            'title': 'Треккинг в Занскаре',
            'destination': dest_dict.get('Занскар'),
            'description': 'Удалённые Гималаи Ладакха.',
            'duration_days': 12,
            'price': 1300.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Палатки',
            'itinerary': 'День 1-12: Трек',
            'available': True,
            'featured': False
        },
        {
            'title': 'Экспедиция в Занскар',
            'destination': dest_dict.get('Занскар'),
            'description': 'Культура и перевалы.',
            'duration_days': 15,
            'price': 1600.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Гид',
            'itinerary': 'День 1-15: Экспедиция',
            'available': True,
            'featured': False
        },
        # 18. Караколь
        {
            'title': 'Треккинг в ущелье Каракол',
            'destination': dest_dict.get('Караколь'),
            'description': 'Ущелья и озёра у Тянь-Шаня.',
            'duration_days': 5,
            'price': 450.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Гид',
            'itinerary': 'День 1-5: Трек',
            'available': True,
            'featured': False
        },
        {
            'title': 'Сноубординг в Караколе',
            'destination': dest_dict.get('Караколь'),
            'description': 'Зимний тур на горнолыжные склоны.',
            'duration_days': 6,
            'price': 600.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Проживание',
            'itinerary': 'День 1-6: Горнолыжка',
            'available': True,
            'featured': False
        },
        # 19. Байкальский хребет
        {
            'title': 'Треккинг по Байкальскому хребту',
            'destination': dest_dict.get('Байкальский хребет'),
            'description': 'Дикие тропы вдоль Байкала.',
            'duration_days': 7,
            'price': 750.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Палатки',
            'itinerary': 'День 1-7: Трек',
            'available': True,
            'featured': False
        },
        {
            'title': 'Каякинг на Байкале',
            'destination': dest_dict.get('Байкальский хребет'),
            'description': 'Сплав по озеру.',
            'duration_days': 5,
            'price': 650.00,
            'difficulty': 'moderate',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Каяки',
            'itinerary': 'День 1-5: Сплав',
            'available': True,
            'featured': False
        },
        # 20. Перуанские Анды
        {
            'title': 'Инкский путь к Мачу-Пикчу',
            'destination': dest_dict.get('Перуанские Анды'),
            'description': 'Классика через джунгли.',
            'duration_days': 4,
            'price': 1200.00,
            'difficulty': 'moderate',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1519671482749-fd09be7ccbf7',
            'includes': '• Лоджи\n• Вход',
            'itinerary': 'День 1: Куско\nДень 2-4: Трек',
            'available': True,
            'featured': True
        },
        {
            'title': 'Трек к Хуайна-Пикчу',
            'destination': dest_dict.get('Перуанские Анды'),
            'description': 'Вид на Мачу-Пикчу с вершины.',
            'duration_days': 5,
            'price': 1300.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1519671482749-fd09be7ccbf7',
            'includes': '• Гид',
            'itinerary': 'День 1-5: Тур',
            'available': True,
            'featured': False
        },
        # 21. Килиманджаро
        {
            'title': 'Восхождение на Килиманджаро',
            'destination': dest_dict.get('Килиманджаро'),
            'description': 'Вершина Африки.',
            'duration_days': 7,
            'price': 2200.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05',
            'includes': '• Портеры\n• Палатки',
            'itinerary': 'День 1-7: Восхождение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Сафари + Килиманджаро',
            'destination': dest_dict.get('Килиманджаро'),
            'description': 'Комбо: сафари и восхождение.',
            'duration_days': 10,
            'price': 2800.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05',
            'includes': '• Сафари\n• Гид',
            'itinerary': 'День 1-10: Комбо',
            'available': True,
            'featured': False
        },
        # 22. Долина Шари
        {
            'title': 'Тур по Долине Шари',
            'destination': dest_dict.get('Долина Шари'),
            'description': 'Оазисы и каньоны Марокко.',
            'duration_days': 5,
            'price': 600.00,
            'difficulty': 'easy',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'includes': '• Отели',
            'itinerary': 'День 1-5: Долина',
            'available': True,
            'featured': False
        },
        {
            'title': 'Сахара + Долина Шари',
            'destination': dest_dict.get('Долина Шари'),
            'description': 'Пустыня и оазисы.',
            'duration_days': 6,
            'price': 800.00,
            'difficulty': 'easy',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'includes': '• Кемп',
            'itinerary': 'День 1-6: Тур',
            'available': True,
            'featured': False
        },
        # 23. Эльбрус
        {
            'title': 'Восхождение на Эльбрус',
            'destination': dest_dict.get('Эльбрус'),
            'description': 'Вершина Европы.',
            'duration_days': 7,
            'price': 950.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Приюты',
            'itinerary': 'День 1-7: Восхождение',
            'available': True,
            'featured': True
        },
        {
            'title': 'Кольцо Эльбруса',
            'destination': dest_dict.get('Эльбрус'),
            'description': 'Обход горы.',
            'duration_days': 8,
            'price': 850.00,
            'difficulty': 'hard',
            'max_group_size': 10,
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'includes': '• Гид',
            'itinerary': 'День 1-8: Кольцо',
            'available': True,
            'featured': False
        },
        # 24. Ладакх
        {
            'title': 'Треккинг в Ладакхе',
            'destination': dest_dict.get('Ладакх'),
            'description': 'Монастыри и высокогорье.',
            'duration_days': 10,
            'price': 1100.00,
            'difficulty': 'hard',
            'max_group_size': 8,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Гостевые дома',
            'itinerary': 'День 1-10: Трек',
            'available': True,
            'featured': False
        },
        {
            'title': 'Мототур по Ладакху',
            'destination': dest_dict.get('Ладакх'),
            'description': 'На мотоциклах по перевалам.',
            'duration_days': 12,
            'price': 1400.00,
            'difficulty': 'moderate',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'includes': '• Мотоциклы',
            'itinerary': 'День 1-12: Тур',
            'available': True,
            'featured': False
        },
        # 25. Тянь-Шань
        {
            'title': 'Треккинг в Тянь-Шане',
            'destination': dest_dict.get('Тянь-Шань'),
            'description': 'Небесные горы и ледники.',
            'duration_days': 8,
            'price': 700.00,
            'difficulty': 'moderate',
            'max_group_size': 12,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Палатки',
            'itinerary': 'День 1-8: Трек',
            'available': True,
            'featured': True
        },
        {
            'title': 'Восхождение на пик Хан-Тенгри',
            'destination': dest_dict.get('Тянь-Шань'),
            'description': 'Семитысячник Тянь-Шаня.',
            'duration_days': 14,
            'price': 2800.00,
            'difficulty': 'hard',
            'max_group_size': 6,
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'includes': '• Снаряжение',
            'itinerary': 'День 1-14: Экспедиция',
            'available': True,
            'featured': False
        },
    ]

    for data in tours_data:
        if data['destination']:
            tour, created = Tour.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                print(f'✓ Создан тур: {tour.title}')


def create_blog_posts():
    """Создание статей блога"""
    posts_data = [
        {
            'title': '10 советов для начинающих путешественников',
            'slug': '10-sovetov-dlya-nachinayushchikh-puteshestvennikov',
            'excerpt': 'Собираетесь в первое большое путешествие? Полезные советы для идеального старта.',
            'content': '''Путешествия обогащают жизнь. Вот 10 советов для новичков:
1. Планируйте заранее, но будьте гибкими.
2. Путешествуйте налегке — меньше вещей, больше свободы.
3. Изучите базовые фразы на местном языке.
4. Обязательно оформите страховку.
5. Делайте копии документов.
6. Будьте открыты новому и местной культуре.
7. Уважайте традиции страны.
8. Следите за бюджетом, но не отказывайтесь от впечатлений.
9. Фотографируйте, но живите моментом.
10. Оставайтесь на связи с близкими, но наслаждайтесь отдыхом.
Каждое путешествие — ваша личная история!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Александр Петров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Лучшие места для треккинга в Центральной Азии',
            'slug': 'luchshie-mesta-dlya-trekkinga-v-tsentralnoy-azii',
            'excerpt': 'Центральная Азия — рай для треккеров. Откройте топ-маршруты.',
            'content': '''Центральная Азия полна потрясающих маршрутов:
- Иссык-Куль (Кыргызстан): озеро и ущелья.
- Фанские горы (Таджикистан): озёра и пики.
- Тянь-Шань: маршруты любой сложности.
Советы: выбирайте лето, берите гида, акклиматизируйтесь, уважайте природу.
Это единение с горами навсегда!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как подготовиться к высокогорному треккингу',
            'slug': 'kak-podgotovitsya-k-vysokogornomu-trekkingu',
            'excerpt': 'Подготовка к высокогорью — ключ к безопасности и успеху.',
            'content': '''Высокогорный треккинг требует подготовки:
Физическая: тренировки за 2–3 месяца (бег, велосипед).
Акклиматизация: поднимайтесь постепенно.
Питание: больше углеводов, пейте воду.
Снаряжение: хорошие ботинки, тёплая одежда.
Медицина: аптечка от горной болезни.
Безопасность превыше всего!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Топ-5 самых красивых озёр мира',
            'slug': 'top-5-samykh-krasivykh-ozer-mira',
            'excerpt': 'От Иссык-Куля до Байкала — самые невероятные озёра для посещения.',
            'content': '''1. Иссык-Куль (Кыргызстан) — жемчужина Тянь-Шаня.
2. Байкал (Россия) — самое глубокое озеро.
3. Титикака (Перу/Боливия) — высочайшее судоходное.
4. Патагонские озёра (Чили) — бирюзовые воды.
5. Лох-Несс (Шотландия) — мистика и природа.
Посетите и почувствуйте магию!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Что взять в поход: полный чек-лист',
            'slug': 'chto-vzyat-v-pokhod-polnyy-chek-list',
            'excerpt': 'Не забудьте ничего важного в треккинге.',
            'content': '''Базовый чек-лист:
- Рюкзак 50–70 л
- Спальник и коврик
- Ботинки и треккинговые палки
- Треккинговые штаны и куртка
- Аптечка и фонарик
- Еда и вода
- Документы и деньги
Соберите заранее — и поход пройдёт гладко!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Грузия: страна вина и гор',
            'slug': 'gruziya-strana-vina-i-gor',
            'excerpt': 'Почему Грузия — must-visit для любителей природы и вина.',
            'content': '''Грузия сочетает Кавказские горы, древние храмы и лучшее вино.
Посетите Казбеги, Сванетию, Кахетию.
Традиции, гостеприимство и вкусная кухня ждут вас!''',
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как преодолеть страх высоты в горах',
            'slug': 'kak-preodolet-strah-vysoty-v-gorakh',
            'excerpt': 'Практические советы для тех, кто боится высоты.',
            'content': '''Страх высоты — распространён.
Советы: медленное дыхание, постепенная акклиматизация, опыт гида.
Многие преодолевают и наслаждаются видами!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Экологичный туризм: как не вредить природе',
            'slug': 'ekologichnyy-turizm-kak-ne-vredit-prirode',
            'excerpt': 'Правила Leave No Trace для ответственных путешественников.',
            'content': '''- Не оставляйте мусор
- Уважайте флору и фауну
- Выбирайте проверенные тропы
- Поддерживайте местные сообщества
Ваше путешествие может быть полезным для планеты!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Патagonia: мечта треккера',
            'slug': 'patagonia-mechta-trekkera',
            'excerpt': 'Почему Patagonia — одно из лучших мест для походов.',
            'content': '''Гранитные башни, ледники, озёра.
W Trek и O Circuit — легенды.
Подготовьтесь к ветру и дождю — стоит того!''',
            'image_url': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470',
            'author': 'Александр Петров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Топ-10 ошибок новичков в горах',
            'slug': 'top-10-oshibok-novichkov-v-gorakh',
            'excerpt': 'Избегайте этих ошибок, чтобы поход прошёл безопасно.',
            'content': '''1. Плохая физподготовка
2. Недооценка погоды
3. Неправильное снаряжение
4. Игнор акклиматизации
5. Переоценка сил
И многие другие — читайте, чтобы не повторить!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Камчатка: земля огня и льда',
            'slug': 'kamchatka-zemlya-ognya-i-lda',
            'excerpt': 'Вулканы, медведи и гейзеры — что посмотреть.',
            'content': '''Камчатка — уникальный регион.
Посетите Долину гейзеров, вулканы, медведей.
Неповторимые впечатления!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как выбрать треккинговые ботинки',
            'slug': 'kak-vybrat-trekkingovye-botinki',
            'excerpt': 'Гид по выбору обуви для гор.',
            'content': '''Критерии: водонепроницаемость, подошва Vibram, фиксация голеностопа.
Примерьте с носками, походите в магазине.
Хорошие ботинки — основа успеха!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Гималаи: от Эвереста до Аннапурны',
            'slug': 'gimalai-ot-everesta-do-annapurny',
            'excerpt': 'Обзор главных треков в Гималаях.',
            'content': '''Эверест Base Camp, Аннапурна Circuit, Лангтанг.
Каждый маршрут — своё приключение.
Готовьтесь к высоте!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Путешествия соло: плюсы и минусы',
            'slug': 'puteshestviya-solo-plyusy-i-minusy',
            'excerpt': 'Почему стоит попробовать путешествовать одному.',
            'content': '''Плюсы: свобода, новые друзья, самопознание.
Минусы: безопасность, одиночество.
Советы: выбирайте проверенные места, делитесь планами.''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Елена Иванова',
            'published': True,
            'featured': False
        },
        {
            'title': 'Кыргызстан: скрытые жемчужины',
            'slug': 'kyrgyzstan-skrytye-zhemchuzhiny',
            'excerpt': 'Кроме Иссык-Куля — что ещё посмотреть.',
            'content': '''Ала-Арча, Сон-Куль, Джеты-Огуз.
Гостеприимство и природа ждут!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как сэкономить на путешествиях',
            'slug': 'kak-sekonomit-na-puteshestviyakh',
            'excerpt': 'Советы по бюджетным поездкам.',
            'content': '''Ловите акции на авиабилеты, выбирайте хостелы, ешьте локально.
Путешествуйте вне сезона.
Больше впечатлений за меньшие деньги!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Фотография в горах: лучшие советы',
            'slug': 'fotografiya-v-gorakh-luchshie-sovety',
            'excerpt': 'Как сделать потрясающие фото в походе.',
            'content': '''Используйте золотой час, штатив, поляризационный фильтр.
Снимайте RAW.
Природа — лучший фотограф!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Альпинизм для начинающих',
            'slug': 'alpinizm-dlya-nachinayushchikh',
            'excerpt': 'Первый шаг в мир альпинизма.',
            'content': '''Начните с простых маршрутов, найдите гида.
Обучение в школе альпинизма.
Безопасность прежде всего!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Культура и традиции в путешествиях',
            'slug': 'kultura-i-traditsii-v-puteshestviyakh',
            'excerpt': 'Как уважать местные обычаи.',
            'content': '''Изучайте этикет, одевайтесь скромно, пробуйте еду.
Это обогащает путешествие!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Рафтинг: адреналин на воде',
            'slug': 'rafting-adrenalin-na-vode',
            'excerpt': 'Как выбрать реку и тур.',
            'content': '''От спокойных до экстремальных.
Алтай, Кыргызстан — отличные варианты.
Сертифицированный гид обязателен!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Зимний туризм: куда поехать',
            'slug': 'zimniy-turizm-kuda-poekhat',
            'excerpt': 'Лучшие места для зимних приключений.',
            'content': '''Камчатка, Байкал, Альпы.
Катание на коньках по льду, снегоходы.
Тепло одевайтесь!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Йога в горах: ретриты',
            'slug': 'yoga-v-gorakh-retrity',
            'excerpt': 'Где провести йога-ретрит.',
            'content': '''Гималаи, Грузия, Кыргызстан.
Природа усиливает практику.
Идеальный отдых!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Елена Иванова',
            'published': True,
            'featured': False
        },
        {
            'title': 'Как выбрать рюкзак для треккинга',
            'slug': 'kak-vybrat-ryukzak-dlya-trekkinga',
            'excerpt': 'Обзор лучших моделей.',
            'content': '''Объём 50–70 л, каркас, пояс.
Тестируйте с нагрузкой.
Комфорт — главное!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Танзания: сафари и Килиманджаро',
            'slug': 'tanzaniya-safari-i-kilimandzharo',
            'excerpt': 'Комбо-тур: животные и вершина.',
            'content': '''Сафари в Серенгети + восхождение.
Незабываемо!''',
            'image_url': 'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05',
            'author': 'Александр Петров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Путешествия с детьми: советы',
            'slug': 'puteshestviya-s-detmi-sovety',
            'excerpt': 'Как сделать поездку комфортной для всей семьи.',
            'content': '''Выбирайте спокойные маршруты, берите перекусы, игры.
Дети — лучшие компаньоны!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Мария Ким',
            'published': True,
            'featured': False
        },
        {
            'title': 'Лучшие приложения для путешественников',
            'slug': 'luchshie-prilozheniya-dlya-puteshestvennikov',
            'excerpt': 'Must-have приложения.',
            'content': '''Google Translate, Maps.me, Booking, Windy.
Всегда под рукой!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Каппадокия: сказочные пейзажи',
            'slug': 'kappadokiya-skazochnye-peyzazhi',
            'excerpt': 'Воздушные шары и подземные города.',
            'content': '''Полёт на шаре на рассвете — магия.
Посетите обязательно!''',
            'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Здоровье в путешествиях: что делать',
            'slug': 'zdorove-v-puteshestviyakh-chto-delat',
            'excerpt': 'Профилактика и первая помощь.',
            'content': '''Вакцины, страховка, аптечка.
Будьте здоровы!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Ладакх: высокогорная пустыня',
            'slug': 'ladakh-vysokogornaya-pustynya',
            'excerpt': 'Монастыри и перевалы.',
            'content': '''Акклиматизация обязательна.
Красота на высоте 4000+ м!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как организовать самостоятельный тур',
            'slug': 'kak-organizovat-samostoyatelnyy-tur',
            'excerpt': 'Пошаговый гид.',
            'content': '''Авиабилеты, жильё, транспорт, маршруты.
Свобода и экономия!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Мария Ким',
            'published': True,
            'featured': False
        },
        {
            'title': 'Турция: Каппадокия и больше',
            'slug': 'turtsiya-kappadokiya-i-bolshe',
            'excerpt': 'От шаров до пляжей.',
            'content': '''Каппадокия, Стамбул, Анталия.
Разнообразие!''',
            'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Медитация в горах',
            'slug': 'meditatsiya-v-gorakh',
            'excerpt': 'Почему горы — идеальное место.',
            'content': '''Тишина, виды, чистый воздух.
Духовное очищение!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Елена Иванова',
            'published': True,
            'featured': False
        },
        {
            'title': 'Топ-10 книг о путешествиях',
            'slug': 'top-10-knig-o-puteshestviyakh',
            'excerpt': 'Книги, которые вдохновят.',
            'content': '''"В диких условиях", "Ешь, молись, люби", "Вокруг света за 80 дней".
Читайте и путешествуйте!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Александр Петров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как пережить джетлаг',
            'slug': 'kak-perezhit-dzhetlag',
            'excerpt': 'Советы по адаптации.',
            'content': '''Свет, вода, мелатонин.
Быстро вернётесь в форму!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Мария Ким',
            'published': True,
            'featured': False
        },
        {
            'title': 'Вулканы мира: куда подняться',
            'slug': 'vulkan-mira-kuda-podnyatsya',
            'excerpt': 'Активные и спящие вулканы.',
            'content': '''Камчатка, Эквадор, Исландия.
Адреналин и виды!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Путешествия в 50+',
            'slug': 'puteshestviya-v-50',
            'excerpt': 'Никогда не поздно!',
            'content': '''Выбирайте комфорт, берите страховку.
Мир ждёт!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Лучшие сувениры из путешествий',
            'slug': 'luchshie-suveniry-iz-puteshestviy',
            'excerpt': 'Что привезти домой.',
            'content': '''Локальные специи, изделия ручной работы.
Не магниты!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Треккинг в Непале: советы',
            'slug': 'trekking-v-nepale-sovety',
            'excerpt': 'Подготовка к Гималаям.',
            'content': '''Акклиматизация, портеры, сезон.
Будьте готовы!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как найти друзей в путешествии',
            'slug': 'kak-nayti-druzey-v-puteshestvii',
            'excerpt': 'Социальные хостелы и туры.',
            'content': '''Хостелы, групповые туры, приложения.
Дружба навсегда!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Елена Иванова',
            'published': True,
            'featured': False
        },
        {
            'title': 'Байкал: зимняя сказка',
            'slug': 'baykal-zimnyaya-skazka',
            'excerpt': 'Лёд и пещеры.',
            'content': '''Катание на коньках, собачьи упряжки.
Неповторимо!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Минимализм в путешествиях',
            'slug': 'minimalizm-v-puteshestviyakh',
            'excerpt': 'Путешествуйте налегке.',
            'content': '''Рюкзак 40 л, многофункциональные вещи.
Свобода!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Сванетия: башни и горы',
            'slug': 'svanetiya-bashni-i-gory',
            'excerpt': 'Средневековая Грузия.',
            'content': '''Местиа, Ушгули, ледники.
История и природа!''',
            'image_url': 'https://images.unsplash.com/photo-1585870406473-3ab4f03c8c17',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как вести дневник путешествий',
            'slug': 'kak-vesti-dnevnik-puteshestviy',
            'excerpt': 'Фиксируйте воспоминания.',
            'content': '''Записывайте, рисуйте, фото.
Ваш личный архив!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Мария Ким',
            'published': True,
            'featured': False
        },
        {
            'title': 'Эльбрус: восхождение на Европу',
            'slug': 'elbrus-voskhozhdenie-na-evropu',
            'excerpt': 'Подготовка к вершине.',
            'content': '''Канатка, приюты, снег.
Достижимо!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': True
        },
        {
            'title': 'Путешествия для души',
            'slug': 'puteshestviya-dlya-dushi',
            'excerpt': 'Места силы.',
            'content': '''Гималаи, Байкал, Алтай.
Энергия природы!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как справляться с высотной болезнью',
            'slug': 'kak-spravlyatsya-s-vysotnoy-boleznyu',
            'excerpt': 'Симптомы и лечение.',
            'content': '''Диакарб, спуск, кислород.
Не игнорируйте!''',
            'image_url': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Турция: от Каппадокии до Ликийской тропы',
            'slug': 'turtsiya-ot-kappadokii-do-likiyskoy-tropy',
            'excerpt': 'Разнообразие природы.',
            'content': '''Шары, пещеры, море.
Всё в одной стране!''',
            'image_url': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        },
        {
            'title': 'Путешествия на машине: road trip',
            'slug': 'puteshestviya-na-mashine-road-trip',
            'excerpt': 'Свобода на колёсах.',
            'content': '''Алтай, Грузия, Камчатка.
Планируйте маршрут!''',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'author': 'Дмитрий Сидоров',
            'published': True,
            'featured': False
        },
        {
            'title': 'Йога-ретриты в Азии',
            'slug': 'yoga-retrity-v-azii',
            'excerpt': 'Лучшие места.',
            'content': '''Индия, Непал, Таиланд.
Душа и тело в гармонии!''',
            'image_url': 'https://images.unsplash.com/photo-1544735716-392fe2489ffa',
            'author': 'Елена Иванова',
            'published': True,
            'featured': True
        },
        {
            'title': 'Как выбрать страховку для путешествий',
            'slug': 'kak-vybrat-strakhovku-dlya-puteshestviy',
            'excerpt': 'Что покрывать.',
            'content': '''Активный отдых, эвакуация, медицина.
Не экономьте!''',
            'image_url': 'https://images.unsplash.com/photo-1482192505345-5655af888cc4',
            'author': 'Александр Петров',
            'published': True,
            'featured': False
        },
        {
            'title': '50 идей для путешествий в 2026 году',
            'slug': '50-idey-dlya-puteshestviy-v-2026-godu',
            'excerpt': 'Вдохновение на год.',
            'content': '''Иссык-Куль, Гималаи, Patagonia и многое другое.
Планируйте сейчас!''',
            'image_url': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828',
            'author': 'Мария Ким',
            'published': True,
            'featured': True
        }
    ]

    for data in posts_data:
        post, created = BlogPost.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if created:
            print(f'✓ Создана статья: {post.title}')

def main():
    print('=' * 60)
    print('Заполнение базы данных тестовыми данными')
    print('=' * 60)
    print()

    print('Создание направлений...')
    destinations = create_destinations()
    print()

    print('Создание туров...')
    create_tours(destinations)
    print()

    print('Создание статей блога...')
    create_blog_posts()
    print()

    print('=' * 60)
    print('✓ Данные успешно загружены!')
    print('=' * 60)
    print()
    print('Теперь вы можете:')
    print('1. Запустить сервер: python manage.py runserver')
    print('2. Открыть сайт: http://127.0.0.1:8000/')
    print('3. Войти в админку: http://127.0.0.1:8000/admin/')
    print()


if __name__ == '__main__':
    main()
