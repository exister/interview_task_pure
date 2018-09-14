# task1

В базе PostgreSQL есть две таблицы. Одна называется Color и содержит название цвета в колонке "name", вторая называется Car и содержит колонку parameters типа jsonb с данными внутри вида: {"price": 9000, "colorId": 1}. Напишите запрос, который выведет количество машин в базе для каждого цвета, содержащегося в таблице Color. Напишите ответ с использованием Django ORM.

task1/cars/models.py/ColorManager.get_cars_count() - возвращает нужные данные

Для запуска:
docker-compose run web python3 manage.py shell_plus
from cars.models import Color
Color.objects.get_cars_count()

# task2

Напишите метод на Python, который принимает на вход список URL'ов изображений, далее параллельно скачивает эти изображения и записывает в MongoDB их URL, ширину и высоту в отдельные документы одной коллекции.

Для запуска:
docker-compose run web
