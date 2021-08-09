import tkinter as tk
from tkinter import ttk, CENTER
class Interfaz:

    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x400")
        self.button = tk.Button(master, text="Newton", height=5, width=30, command=self.newton())
        self.button2 = tk.Button(master, text="Interpolacion", height=5, width=30, command=self.Interpolacion())
        self.button.place(relx=0.5, rely=.25, anchor=CENTER)
        self.button2.place(relx=0.5, rely=.5, anchor=CENTER)

    def newton(self):
        
        pass

    def Interpolacion(self):
        pass


root = tk.Tk()
app = Interfaz(root)
root.eval('tk::PlaceWindow . center')
root.mainloop()