import sqlite3
import tkinter as tk
import random
from tkinter import ttk

def insert_package():
    name = tname_fill.get()
    price = float(tprice_fill.get())
    k = []
    for i in range(4):
        k.append(random.randint(1, 9))

    package_info = (1,name,price,k[0],k[1],k[2],k[3])
    with sqlite3.connect('C:\\Users\\chees\\OneDrive\\Рабочий стол\\drive\\db\\dostavka.db') as db:
        cursor = db.cursor()
        query = """insert into packages(free, name, price, x1, y1, x2, y2) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query,package_info)
        db.commit()
        #open_window()

def add_package():
    if not hasattr(add_package, 'new_window') or not add_package.new_window.winfo_exists():
        add_package.new_window = tk.Toplevel()
        add_package.new_window.title("Добавить посылку")
        action_open(add_package.new_window)
    else:
        add_package.new_window.lift()

def action_open(new_window):

    new_window.geometry("300x200")
    form_add = tk.Frame(new_window)    
    buts = tk.Frame(new_window)
    tname = tk.Label(form_add,text="Название:")
    global tname_fill
    tname_fill = tk.Entry(form_add)
    tprice = tk.Label(form_add,text="Цена:")
    global tprice_fill
    tprice_fill = tk.Entry(form_add)

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
    tprice_fill.pack()

    b_add.pack(side="left",padx=10)
    b_close.pack(side="left",padx=10)

    form_add.pack(expand=True)
    buts.pack(expand=True)   