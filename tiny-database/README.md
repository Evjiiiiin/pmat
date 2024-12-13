# tiny-sql
Минималистичная СУБД, хранящаяся в CSV.


## Установка poetry
Можно использовать любой другой инструмент для управления зависимостями и виртуальными окружениями.
```aiignore
curl -sSL https://install.python-poetry.org | python3 -
```
## Задание №1
1. В таблицу **EmployeeTable** внести индекс _department_id_.
2. Добавить функцию select для **DepartmentTable** по названию подразделения (возвращать список, т.к. таких может быть несколько)
2. Сделать проверку на то, что в каждой из таблиц присутствуют только уникальные наборы индексов по кортежам.
   То есть в таблице **EmployeeTable** не должно присутствовать ни одной записи с одинаковыми _id_ и _department_id_:
если для любых двух записей в таблице EmployeeTable _position_1_ == _position_2_ и _department_id_1_ == _department_id_2_, тогда это одни и
   те же записи (по сути условие уникального композитного индекса). Для таблицы **DepartmentTable** гарантировать, что нет двух
   записей с одинаковыми _department_id_.
3. Реализовать в **Database** классе функцию _join_, которая будет объядинять таблицы по полям '_DepartmentTable.department_id_' и
'_EmployeeTable.department_id_'.
4. Написать тесты:
   1. На проверку уникальных индексов для пункта 2,
   2. Тест для проверки правильности операции **JOIN** из пункта 3.
   3. Удостовериться, что .csv файлы отсутствуют.

## Задание №2

1. Добавить третью таблицу (к примеру с товарами (Goods)), определить её аттрибуты, индексы итд.
2. Написать и оттестировать запрос, содержащий 2 JOIN операции и aggregate (AVG, MAX, MIN, COUNT).
3. Реализовать aggregate функцию.
4. Обобщить primary и unique индекс, и проверку на них - доп. балл.*

## Задание 3

1. Установите pre-commit. Напишите .pre-commit-config.yaml файл, добавьте хуки по умолчанию, которые считает нужными.
2. Добавить хуки flake8, black, isort, pytest.
3. Добавьте проверку, что commit проходит только при покрытии кода в 100% (--cov-fail-under=100).
4. Создайте workflow в Github Actions, с задачей, которая прогоняет ваши тесты. Аналогично, добавьте проверку на покрытие кода в 100%.

## Комманды
Запустить тесты c покрытием кода:
```
poetry run pytest --cov
```