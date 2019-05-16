
__author__ = 'Белинский Андрей Петрович'

""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import os
import requests
import datetime
import json
import re
import sqlite3


class Weather:

    weather_url = 'http://api.openweathermap.org/data/2.5/'
    path_app_id = os.path.join('data', 'app.id')
    path_bd = os.path.join('data', 'weather.db')
    path_city_lst = os.path.join('data', 'city.list.json')

    @staticmethod
    def __add__id():

        with open(Weather.path_app_id, 'r', encoding='UTF-8') as file:
            app_id = file.read()
        return app_id

    @staticmethod
    def _create_bd():

        if not os.path.isfile(Weather.path_bd):
            with sqlite3.connect(Weather.path_bd) as conn:
                conn.execute("""
                    create table Погода (
                        id_города           INTEGER PRIMARY KEY,
                        Город               VARCHAR(255),
                        Дата                DATE,
                        Температура         INTEGER,
                        id_погоды           INTEGER
                    );
                    """)
            return True
        else:
            return False

    @staticmethod
    def _add_in_bd(bd_dct):

        try:
            with sqlite3.connect(Weather.path_bd) as conn:
                conn.execute("""
                    insert into Погода (id_города, Город, Дата, Температура, id_погоды) VALUES (?,?,?,?,?)""", (
                        bd_dct['id'],
                        bd_dct['name'],
                        datetime.date.today(),
                        bd_dct['main']['temp'],
                        bd_dct['weather'][0]['id']))
            return True
        except sqlite3.IntegrityError:
            return False

    @staticmethod
    def _check_bd(city_id):

        with sqlite3.connect(Weather.path_bd) as conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM Погода WHERE id_города=?"
            cursor.execute(sql, [city_id])

            if cursor.fetchone():
                return True
            else:
                return False

    @staticmethod
    def _update_bd(bd_dct):

        try:
            with sqlite3.connect(Weather.path_bd) as conn:
                cur = conn.cursor()
                cur.execute("update Погода set Температура=:Температура and Дата=:Дата where id_города=:id_города",
                            {'Температура': bd_dct['main']['temp'],
                             'Дата': datetime.date.today(),
                             'id_города': bd_dct['id']})
            return True
        except sqlite3.IntegrityError:
            return False

    @staticmethod
    def add_city_id(country, city):

        city_id = False
        with open(Weather.path_city_lst, 'r', encoding='UTF-8') as file:
            tmp = json.loads(file.read())

        for itm in tmp:
            if itm['country'] == country.upper() and itm['name'] == city.title():
                city_id = itm['id']
                break
        return city_id

    @staticmethod
    def get_weather_data(city_ids):
        city_id_lst = ''

        if type(city_ids) == list:
            part_url = 'group'

            for city_id in city_ids:
                if not city_id.isdigit():
                    city_id = Weather.add_city_id(city_id)
                city_id_lst += str(city_id) + ','
        else:
            part_url = 'weather'
            city_id_lst += str(city_ids) + ','

        full_url = Weather.weather_url + f'{part_url}?id={city_id_lst[:-1]}&units=metric&appid={Weather.__add__id()}'

        try:
            response = requests.get(full_url)
            if response.status_code != 200:
                return False
            else:
                weather_data = response.json()
                return weather_data

        except requests.exceptions.RequestException:
            return False

    @staticmethod
    def add_data_in_bd(data):
        if type(data) is not False:
            Weather._create_bd()
            if 'cnt' in data:
                for itm in data['list']:
                    if Weather._check_bd(itm['id']):
                        Weather._update_bd(itm)
                    else:
                        Weather._add_in_bd(itm)
            else:
                if Weather._check_bd(data['id']):
                    Weather._update_bd(data)
                else:
                    Weather._add_in_bd(data)
        else:
            return False
        return True

    @staticmethod
    def get_list_country():

        lst_country = set()
        with open(Weather.path_city_lst, 'r', encoding='UTF-8') as file:
            tmp = json.loads(file.read())
        for itm in tmp:
            if itm['country']:
                lst_country.add(itm['country'])
        return sorted(list(lst_country))

    @staticmethod
    def get_list_city(country, city='\w+'):

        city_lst = []
        patt_country = country.upper()
        patt_city = re.compile('^' + city.title() + '+.*')
        with open(Weather.path_city_lst, 'r', encoding='UTF-8') as file:
            tmp = json.loads(file.read())
        for itm in tmp:
            if itm['country'] == patt_country and patt_city.findall(itm['name']):
                city_lst.append(patt_city.findall(itm['name'])[0])
        return city_lst

    @staticmethod
    def get_weather(country, *city):
        ans = ''
        for itm in city:
            id_city = Weather.add_city_id(country, itm)
            if id_city is not False:
                dat = Weather.get_weather_data(id_city)
                Weather.add_data_in_bd(dat)
                temp = dat['main']['temp']
                wind = dat['wind']['speed']
                ans += f"В городе {itm} температура {temp} С, скорость ветра {wind} м/с\n"
            else:
                ans += 'Такого города не существует\n'
        return ans


if __name__ == '__main__':
    print(Weather.get_list_city('RU', 'Mos'))
    print(Weather.get_weather('RU', 'Moskva', 'Norilsk', 'Saint Petersburg'))

"""
# структура словарей openweather

a = {'coord': {'lon': 88.2, 'lat': 69.35},
     'weather': [{'id': 620,
                  'main': 'Snow',
                  'description': 'light shower snow',
                  'icon': '13d'}],
     'base': 'stations',
     'main': {'temp': -6,
              'pressure': 1005,
              'humidity': 92,
              'temp_min': -6,
              'temp_max': -6},
     'visibility': 8000,
     'wind': {'speed': 9,
              'deg': 190},
     'clouds': {'all': 75},
     'dt': 1556805600,
     'sys': {'type': 1,
             'id': 8951,
             'message': 0.0049,
             'country': 'RU',
             'sunrise': 1556743482,
             'sunset': 1556810617},
     'id': 1497337,
     'name': 'Norilsk',
     'cod': 200}


b = {'cnt': 2,
     'list': [{'coord': {'lon': 88.2,
                         'lat': 69.35},
               'sys': {'type': 1,
                       'id': 8951,
                       'message': 0.0049,
                       'country': 'RU',
                       'sunrise': 1556743482,
                       'sunset': 1556810617},
               'weather': [{'id': 620,
                            'main': 'Snow',
                            'description': 'light shower snow',
                            'icon': '13d'}],
               'main': {'temp': -6,
                        'pressure': 1005,
                        'humidity': 92,
                        'temp_min': -6,
                        'temp_max': -6},
               'visibility': 8000,
               'wind': {'speed': 9,
                        'deg': 190},
               'clouds': {'all': 75},
               'dt': 1556809493,
               'id': 1497337,
               'name': 'Norilsk'},
              {'coord': {'lon': -75.52,
                         'lat': 41.34},
               'sys': {'type': 1,
                       'id': 4462,
                       'message': 0.0107,
                       'country': 'US',
                       'sunrise': 1556791100,
                       'sunset': 1556841580},
               'weather': [{'id': 701,
                            'main': 'Mist',
                            'description': 'mist',
                            'icon': '50d'}],
               'main': {'temp': 17.3,
                        'pressure': 1022,
                        'humidity': 87,
                        'temp_min': 15,
                        'temp_max': 20},
               'visibility': 4828,
               'wind': {'speed': 1.5,
                        'deg': 300},
               'clouds': {'all': 90},
               'dt': 1556809493,
               'id': 5202009,
               'name': 'Moscow'}]}
"""
