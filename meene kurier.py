import sqlite3
import tkinter as tk
from tkinter import ttk

def add_record():
    conn = sqlite3.connect('db/dostavka.db')
    cursor = conn.cursor()
    data = [
    (0,"Диана",3,4,9),
    (0,"Семён",2,1,5),
    (1,"Сайаана",8,9,20)
    ]
    
    # query = """CREATE TABLE IF NOT EXISTS kurier(free INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, x1 INTEGER, y1 INTEGER, v INTEGER)"""
    # cursor.execute(query)
    cursor.executemany("INSERT INTO kurier (free, name, x1, y1, v) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def delete_table():
    import sqlite3

    # Подключение к базе данных
    conn = sqlite3.connect('db/dostavka.db')

    # Создание объекта курсора
    cursor = conn.cursor()

    # Удаление таблицы
    cursor.execute("DROP TABLE IF EXISTS packages")

    # Применение изменений в базе данных
    conn.commit()

    # Закрытие соединения
    conn.close()


add_record()
# delete_table()