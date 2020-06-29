from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('clock')
def time():
    string=strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
lbl=Label(root,font=('calibri',50,'bold'),
          background='black',
          foreground='orange')
lbl.pack(anchor='center')
time()

mainloop()
    
