import sqlite3
import tkinter as tk
from tkinter import ttk

def add_record():
    conn = sqlite3.connect('db/dostavka.db')
    cursor = conn.cursor()
    data = [
    (1,"Посылка 0",900,1,1,1,9),
    (1,"Посылка 1",1500,2,4,9,9),
    (1,"Посылка 2",300,2,3,9,8)
    ]
    
    query = """CREATE TABLE IF NOT EXISTS packages(free INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, x1 INTEGER, y1 INTEGER, x2 INTEGER, y2 INTEGER)"""
    cursor.execute(query)
    cursor.executemany("INSERT INTO packages (free, name, price, x1, y1, x2, y2) VALUES (?, ?, ?, ?, ?, ?, ?)", data)
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