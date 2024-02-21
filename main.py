from tkinter import *
from windows.win_kur import open_window as kur_open
from windows.win_pack import open_window as pack_open
from windows.win_raspr import open_window as raspr_open


root = Tk()
root.title("Доставка посылок")
root.geometry("1000x600")
root.resizable(width=False,height=False)
root.iconbitmap('iconic.ico')
root.config(bg = "skyblue")


btn1 = Button(root, 
              text = 'Список посылок',
              command = pack_open,
              font = 'Roboto 27'
              )
btn2 = Button(root, 
              text = 'Список курьеров',
              command = kur_open,
              font = 'Roboto 27'
            )
btn3 = Button(root, text = 'Распределить',
              command = raspr_open,
              font = 'Roboto 27'
              )

btn1.pack(expand=True)
btn2.pack(expand=True)
btn3.pack(expand=True)

root.mainloop()