import sqlite3
import tkinter as tk
import random
from tkinter import ttk

def insert_package():
    name = tname_fill.get()
    v = float(tv_fill.get())
    k = []
    for i in range(2):
        k.append(random.randint(1, 9))

    package_info = (1,name,k[0],k[1],v)
    with sqlite3.connect('C:\\Users\\chees\\OneDrive\\Рабочий стол\\drive\\db\\dostavka.db') as db:
        cursor = db.cursor()
        query = """insert into kurier(free, name, x1, y1, v) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query,package_info)
        db.commit()
        #open_window()

def add_kurier():
    if not hasattr(add_kurier, 'new_window') or not add_kurier.new_window.winfo_exists():
        add_kurier.new_window = tk.Toplevel()
        add_kurier.new_window.title("Добавить посылку")
        action_open(add_kurier.new_window)
    else:
        add_kurier.new_window.lift()

def action_open(new_window):

    new_window.geometry("300x200")
    form_add = tk.Frame(new_window)    
    buts = tk.Frame(new_window)
    tname = tk.Label(form_add,text="Имя:")
    global tname_fill
    tname_fill = tk.Entry(form_add)
    tprice = tk.Label(form_add,text="Скорость:")
    global tv_fill
    tv_fill = tk.Entry(form_add)

    b_add = tk.Button(buts,
                        text='Добавить',
                        command=insert_package
                       )
    b_close = tk.Button(buts,
                        text='Закрыть',
                        command=new_window.destroy
                       )
    
    tname.pack()
    tname_fill.pack()
    tprice.pack()
    tv_fill.pack()

    b_add.pack(side="left",padx=10)
    b_close.pack(side="left",padx=10)

    form_add.pack(expand=True)
    buts.pack(expand=True)   