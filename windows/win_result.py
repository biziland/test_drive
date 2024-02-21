import tkinter as tk
from tkinter import ttk

def open_result(ras):
    win = tk.Toplevel()
    win.title("Результат")
    table = ttk.Treeview(win,show='headings')
    heads = ['id посылки', 'id курьера']
    table['columns'] = heads
    
    table.column('#0', width=50)
    table.column('id посылки', width=150)
    table.column('id курьера', width=150)
    

    for h in heads:
        table.heading(h,text=h,anchor='center')
        table.column(h,anchor='center')


    for row in ras:
        table.insert('', 'end', values=row[0:])



  
    # win.pack(expand=True)   
    scroll_pane = ttk.Scrollbar(win,command=table.yview)
    scroll_pane.pack(side=tk.RIGHT,fill=tk.Y)
    table.configure(yscrollcommand=scroll_pane.set)
    table.pack(expand=tk.YES,fill=tk.BOTH)