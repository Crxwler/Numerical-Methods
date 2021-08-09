import tkinter as tk
from tkinter import ttk, CENTER


class InterfazInterpolacion:

    def __init__(self, master):
        self.text = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.master = master
        master.title("Interpolacion")
        master.geometry("600x400")
        # Datos de x
        self.label = tk.Label(master, text="El punto en X")
        self.label.place(x=50, y=20)
        self.entry = ttk.Entry(master, textvariable=self.text)
        self.entry.place(x=50, y=50)
        # Datos de y
        self.label2 = tk.Label(root, text="El punto en y")
        self.label2.place(x=200, y=20)
        self.entry2 = ttk.Entry(master, textvariable=self.text2)
        self.entry2.place(x=200, y=50)
        # Datos del valor a evaluar
        self.label3 = tk.Label(master, text="Dato a ser evaluado")
        self.label3.place(x=350, y=20)
        self.entry3 = ttk.Entry(master, textvariable=self.text3)
        self.entry3.place(x=350, y=50)
        # Botones
        self.button = tk.Button(root, text="Agregar", command=self.agregar)
        self.button.place(x=50, y=80)
        self.button2 = tk.Button(root, text="Calcular", command=self.calcular)
        self.button2.place(x=200, y=80)
        self.button2 = tk.Button(master, text="Regresar", command=self.regresar)
        self.button2.place(x=350, y=80)
        # Create an object of Style widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Add a Treeview widget
        self.tree = ttk.Treeview(master, column=("x", "y"),
                                 show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="x")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="y")
        self.tree.place(x=50, y=200)
        # self.place(width=1100, height=400)

    def calcular(self):
        print("Calculate")
        data = self.text.get()
        data2 = self.text2.get()
        data3 = self.text3.get()
        print(data, data2, data3)
        print(self.text.get(), self.text2.get(), self.text3.get())
        return None

    def agregar(self):
        print("ADD")
        data = self.text.get()
        data2 = self.text2.get()
        data3 = self.text3.get()
        print(data, data2, data3)
        print(self.text.get(), self.text2.get(), self.text3.get())
        return None

    def regresar(self):
        print("RETURN")
        data = self.text.get()
        data2 = self.text2.get()
        data3 = self.text3.get()
        print(data, data2, data3)
        print(self.text.get(), self.text2.get(), self.text3.get())
        return None


root = tk.Tk()
root.eval('tk::PlaceWindow . center')
app = InterfazInterpolacion(root)
root.mainloop()
