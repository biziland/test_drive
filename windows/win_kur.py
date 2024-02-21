import sqlite3
import tkinter as tk
from tkinter import ttk
from forms.add_kur import add_kurier

def update_table():
    conn = sqlite3.connect('db/dostavka.db')
    cursor = conn.cursor()

    # Выполнение SQL-запроса для выборки данных из таблицы
    cursor.execute("SELECT id, name, x1, y1, v FROM kurier")
    rows = cursor.fetchall()

    # Очистка содержимого таблицы
    for i in table.get_children():
        table.delete(i)

    # Вставка данных в таблицу
    for row in rows:
        table.insert('', 'end', values=row)

    # Закрытие соединения
    conn.close()


def get_data():
    all_data = []
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT id, name, x1, y1, v FROM kurier"""
        cursor.execute(query)
        all_data = cursor
    return all_data

def open_window():
    if not hasattr(open_window, 'new_window') or not open_window.new_window.winfo_exists():
        open_window.new_window = tk.Toplevel()
        open_window.new_window.title("Курьеры")
        action_open(open_window.new_window)
    else:
        open_window.new_window.lift()

def action_open(new_window):

    new_window.geometry("800x400")

    header = tk.Frame(new_window)
    b_add = tk.Button(header,
                      text='Добавить курьера',
                      command=add_kurier)
    b_edit = tk.Button(header,
                       text='Обновить таблицу',
                       command=update_table)

    b_edit.pack(side="left",padx=10)  
    b_add.pack(side="left",padx=10)
    header.pack(expand=True)


    body = tk.Frame(new_window,bg='white')

    new_label = tk.Label(body, text="Список курьеров",bg='white')
    new_label.pack()
    
    data = get_data()
    global table
    table = ttk.Treeview(body,show='headings')
    heads = ['id', 'name','x1', 'y1', 'v']
    table['columns'] = heads
    
    table.column('#0', width=50)
    table.column('id', width=50)
    table.column('name', width=150)
    table.column('x1', width=50)
    table.column('y1', width=50)
    table.column('v', width=50)
    

    for h in heads:
        table.heading(h,text=h,anchor='center')
        table.column(h,anchor='center')


    for row in data:
        table.insert('', 'end', values=row[0:])



  
    body.pack(expand=True)   
    scroll_pane = ttk.Scrollbar(body,command=table.yview)
    scroll_pane.pack(side=tk.RIGHT,fill=tk.Y)
    table.configure(yscrollcommand=scroll_pane.set)
    table.pack(expand=tk.YES,fill=tk.BOTH)
