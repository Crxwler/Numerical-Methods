import tkinter as tk
from tkinter import ttk, CENTER

import InterfazNewton

class Menu:
    def __init__(self, master):
        root.title("Calculadora")
        root.geometry("400x400")
        principal = tk.Frame(root)
        button = tk.Button(principal, text="Newton", height=5, width=30, command=self.newton)
        button2 = tk.Button(principal, text="Interpolacion", height=5, width=30, command=self.Interpolacion)
        button.place(relx=0.5, rely=.25, anchor=CENTER)
        button2.place(relx=0.5, rely=.5, anchor=CENTER)

    def newton(self):
        obj = InterfazNewton.InterfazNewton()
        pass

    def Interpolacion(self):
        pass


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
app = Menu(root)
root.mainloop()
