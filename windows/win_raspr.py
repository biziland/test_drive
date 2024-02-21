import sqlite3
import tkinter as tk
from tkinter import *
from windows.win_result import open_result
from algor.final import thirdtry

# - распределить посылки по курьерам
#     - появляется окно со свободными курьерами и новыми посылками (не помеченными), иначе окно "новых посылок нет!" или "свободных курьеров нет"!
#     - чекбокс "приоритет по минимальному максимальному времени"
#         - запускается программа thirdtry/secondtry и выводится результат в виде окна
#         - обновляется бд

def open_window():
    if not hasattr(open_window, 'new_window') or not open_window.new_window.winfo_exists():
        open_window.new_window = tk.Toplevel()
        open_window.new_window.title("Распределение")
        action_open(open_window.new_window)
    else:
        open_window.new_window.lift()

def get_pack_table(fp):
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT id, name, price, x1, y1, x2, y2 FROM packages where free = 1"""
        cursor.execute(query)
        all_data = cursor
    
    if all_data:
        table = tk.ttk.Treeview(fp,show='headings')
        heads = ['id', 'name', 'price', 'x1', 'y1', 'x2', 'y2']
        table['columns'] = heads
        
        table.column('#0', width=50)
        table.column('id', width=50)
        table.column('name', width=150)
        table.column('price', width=80)
        table.column('x1', width=50)
        table.column('y1', width=50)
        table.column('x2', width=50)
        table.column('y2', width=50)
        

        for h in heads:
            table.heading(h,text=h,anchor='center')
            table.column(h,anchor='center')


        for row in all_data:
            table.insert('', 'end', values=row[0:])
    
        scroll_pane = tk.ttk.Scrollbar(fp,command=table.yview)
        scroll_pane.pack(side=tk.RIGHT,fill=tk.Y)
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=tk.YES,fill=tk.BOTH)
    else:
        fp_none = tk.Label(fp,text="Свободных посылок нет! Отдыхайте")
        fp_none.pack()

def get_kur_table(fp):
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT id, name, x1, y1, v FROM kurier where free = 1"""
        cursor.execute(query)
        all_data = cursor
    
    if all_data:
        table = tk.ttk.Treeview(fp,show='headings')
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

        for row in all_data:
            table.insert('', 'end', values=row[0:])
    
        scroll_pane = tk.ttk.Scrollbar(fp,command=table.yview)
        scroll_pane.pack(side=tk.RIGHT,fill=tk.Y)
        table.configure(yscrollcommand=scroll_pane.set)
        table.pack(expand=tk.YES,fill=tk.BOTH)
    else:
        fp_none = tk.Label(fp,text="Свободных курьеров нет! Подождите пока кто-нибудь освободится")
        fp_none.pack()

def get_algo():
    l_kur=[]
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT id, name, x1, y1, v FROM kurier where free = 1"""
        cursor.execute(query)
        l_kur = cursor.fetchall()
    l_pack=[]
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT id, name, price, x1, y1, x2, y2 FROM packages where free = 1"""
        cursor.execute(query)
        l_pack = cursor.fetchall()
    
    if l_pack and l_kur:
        res = thirdtry(l_kur,l_pack)
        open_result(res)
        set_table_pack(res)
        set_table_kur(res)
    else:
        print("Свободных посылок или курьеров нет!")

def set_table_pack(res):
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        for i in res:
            query = "UPDATE packages SET free = 0 WHERE id = ?"
            cursor.execute(query, (i[0],))
        # query = "UPDATE packages SET free = 1"
        # cursor.execute(query)
        
def set_table_kur(res):
    with sqlite3.connect('db/dostavka.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        for i in res:
            query = "UPDATE kurier SET free = 0 WHERE id = ?"
            cursor.execute(query, (i[1],))
        # query = "UPDATE kurier SET free = 1"
        # cursor.execute(query)




def action_open(new_window):    
    #new_window.geometry("800x400")
    fk = tk.Frame(new_window, width=200,height=400)
    fp = tk.Frame(new_window, width=200,height=400)
    sub_frame = tk.Frame(new_window,width=400,height=300)

    k_label = tk.Label(fk, text="Список свободных курьеров",bg='white')
    k_label.pack()
    get_kur_table(fk)
    
    p_label = tk.Label(fp, text="Список свободных посылок",bg='white')
    p_label.pack()
    get_pack_table(fp)

    b_raspr = tk.Button(sub_frame, text="Распределить",command=get_algo)
    b_raspr.pack(expand=True)


    
    fk.grid(row=0,column=0)
    fp.grid(row=0,column=1)
    sub_frame.grid(row=1,column=0,columnspan=2)
    # fk.pack()
    # fp.pack()

    pass