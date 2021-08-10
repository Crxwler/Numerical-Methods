import tkinter as tk
from tkinter import ttk, CENTER

import InterfazNewton

class Menu(tk.Frame):

    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x400")
        # Botones
        self.button = tk.Button(master, text="Newton", height=5, width=30, command=self.callNewton)
        self.button2 = tk.Button(master, text="Interpolacion", height=5, width=30, command=self.callInterpolation)
        self.button.place(relx=0.5, rely=.25, anchor=CENTER)
        self.button2.place(relx=0.5, rely=.5, anchor=CENTER)

    def callNewton(self):
        self.newtonView = tk.Toplevel(self.master)
        self.app = InterfazNewton(self.newtonView)


    def callInterpolation(self):

        pass


root = tk.Tk()
app = Menu(root)
root.mainloop()
