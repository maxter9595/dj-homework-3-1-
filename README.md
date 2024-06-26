# Алгоритм запуска проекта

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Убедитесь, что в settings.py правильно указаны параметры для подключения к базе данных (БД):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_import_phones',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}
```

3. Создайте БД с именем, указанным в NAME (netology_import_phones):
```bash
createdb -U postgres netology_import_phones
```

4. Осуществите команды для создания миграций приложения с БД:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Загрузите данные из csv в БД:
```bash
python manage.py import_phones
```

6. Запустите приложение:
```bash
python manage.py runserver
```


# Текст основного задания ("Знакомство с базами данных")

## Задание

Есть некоторый [csv-файл](./phones.csv), который выгружается с сайта-партнера. Этот сайт занимается продажей телефонов.
Мы же являемся их региональными представителями, поэтому нам необходимо взять данные из этого файла и отобразить 
их на нашем сайте на странице каталога, с их предварительным сохранением в базу данных.

## Реализация

Что необходимо сделать:
* В файле `models.py` нашего приложения создаем модель Phone с полями `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`. Поле `id` - должно быть основным ключом модели.
* Значение поля `slug` должно устанавливаться слагифицированным значением поля `name`.
* Написать скрипт для переноса данных из csv-файла в модель `Phone`. 
Скрипт необходимо разместить в файле `import_phones.py` в методе `handle(self, *args, **options)`
* При запросе `<имя_сайта>/catalog` - должна открываться страница с отображением всех телефонов.
* При запросе `<имя_сайта>/catalog/iphone-x` - должна открываться страница с отображением информации по телефону.
* В каталоге необходимо добавить возможность менять порядок отображения товаров: по названию (в алфавитном порядке) и по цене (по-убыванию и по-возрастанию).

## Подсказка

Для переноса данных из файла в модель можно выбрать один из способов:
 * воспользоваться стандартной библиотекой языка python : `csv` (рекомендуется)
 * построчно пройтись по файлу и для каждой строки сделать соответствующую запись в БД
 
Для реализации сортировки можно к урлу добавить параметр sort и получать его через `request.GET`. Например:
 * `<имя_сайта>/catalog?sort=name` - сортировка по названию
 * `<имя_сайта>/catalog?sort=min_price` - сначала отображать дешевые

## Документация по проекту

Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для загрузки данных из csv в БД
```bash
python manage.py import_phones
```

* Команда для запуска приложения
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```

![Каталог с телефонами](res/catalog.png)
