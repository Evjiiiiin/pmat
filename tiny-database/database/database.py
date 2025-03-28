import csv
import os
from abc import ABC, abstractmethod


class SingletonMeta(type):
    """Синглтон метакласс для Database."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """Класс-синглтон базы данных с таблицами, хранящимися в файлах."""

    def __init__(self):
        self.tables = {}

    def register_table(self, table_name, table):
        self.tables[table_name] = table

    def insert(self, table_name, data):
        table = self.tables.get(table_name)
        if table:
            table.insert(data)
        else:
            raise ValueError(f"Table {table_name} does not exist.")

    def select(self, table_name, *args):
        table = self.tables.get(table_name)
        return table.select(*args) if table else None

    def join(
        self, table1_name, table2_name, join_attr="id", join_attr2="department_id"
    ):

        table_1 = self.tables.get(table1_name)
        table_2 = self.tables.get(table2_name)

        if not table_1 or not table_2:
            raise ValueError("First or both of tables are not exist.")

        joined_data = []
        for row_1 in table_1.data:
            for row_2 in table_2.data:
                if row_1[join_attr] == row_2[join_attr]:
                    joined_data.append({**row_1, **row_2})

        return joined_data


class Table(ABC):
    """Абстрактный базовый класс для таблиц с вводом/выводом файлов CSV."""

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def select(self, *args):
        pass


class EmployeeTable(Table):
    """Таблица сотрудников с методами ввода-вывода из файла CSV."""

    ATTRS = ("id", "name", "age", "salary")
    FILE_PATH = "employee_table.csv"

    def __init__(self):
        self.data = []
        self.load()  # Подгружаем из CSV-файла сразу при инициализации

    def insert(self, data):
        entry = dict(zip(self.ATTRS, data.split()))
        self.data.append(entry)
        self.save()

    def select(self, start_id, end_id):
        return [entry for entry in self.data if start_id <= int(entry["id"]) <= end_id]

    def save(self):
        with open(self.FILE_PATH, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []


class DepartmentTable(Table):
    """Таблица подразделенией с вводлм-выводом в/из CSV файла."""

    ATTRS = ("id", "department_name")
    FILE_PATH = "department_table.csv"

    def __init__(self):
        self.data = []
        self.load()

    # TODO: Реализовать
    def select(self, department_name):
        pass

    def insert(self, data):
        entry = dict(zip(self.ATTRS, data.split()))
        self.data.append(entry)
        self.save()

    def save(self):
        with open(self.FILE_PATH, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []
