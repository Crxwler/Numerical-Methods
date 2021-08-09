import tkinter as tk
from tkinter import ttk, CENTER

import InterfazNewton


def menu():
    InterfazNewton.pack_forget()
    principal.pack(side="top", fill="both", expand=True)


def newton():
    principal.pack_forget()
    InterfazNewton.pack(side="top", fill="both", expand=True)


def Interpolacion():
    pass


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.title("Calculadora")
root.geometry("400x400")
principal = tk.Frame(root)
button = tk.Button(principal, text="Newton", height=5, width=30, command=newton())
button2 = tk.Button(principal, text="Interpolacion", height=5, width=30, command=Interpolacion())
button.place(relx=0.5, rely=.25, anchor=CENTER)
button2.place(relx=0.5, rely=.5, anchor=CENTER)
root.mainloop()
