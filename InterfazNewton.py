import tkinter as tk
from tkinter import ttk, CENTER


class InterfazNewton:

    def __init__(self, master):
        self.master = master
        master.title("Newton")
        master.geometry("1100x400")
        # Crear caja de texto.
        # Expresion.
        self.label = tk.Label(master, text="introduzca la expresion")
        self.label.place(x=50, y=20)
        self.entry = ttk.Entry(root)
        self.entry.place(x=50, y=50)
        #Datos de X0
        self.label2 = tk.Label(root, text="El valor de x(0)")
        self.label2.place(x=200, y=20)
        self.entry2 = ttk.Entry(master)
        self.entry2.place(x=200, y=50)
        #Datos de la cantidad de resultados
        self.label3 = tk.Label(master, text="cantidad de veces")
        self.label3.place(x=350, y=20)
        self.entry3 = ttk.Entry(master)
        self.entry3.place(x=350, y=50)
        #Datos del numero maximo
        self.label4 = tk.Label(master, text="hasta que numero")
        self.label4.place(x=500, y=20)
        self.entry4 = ttk.Entry(master)
        self.entry4.place(x=500, y=50)
        # Posicionarla en la ventana.
        self.entry3.place(x=350, y=50)
        self.button = tk.Button(master, text="Calcular", command=self.calcular)
        self.button.place(x=350, y=150)
        # Create an object of Style widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Add a Treeview widget
        self.tree = ttk.Treeview(master, column=("xn", "yn", "valor real", "valor absoluto", "Error relativo"),
                                 show='headings', height=5)
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="xn")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="yn")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="valor real")
        self.tree.column("# 4", anchor=CENTER)
        self.tree.heading("# 4", text="valor absoluto")
        self.tree.column("# 5", anchor=CENTER)
        self.tree.heading("# 5", text="Error relativo")
        self.tree.place(x=50, y=200)
        # self.place(width=1100, height=400)

    def calcular(self):
        selected = int(self.selected.get())
        if selected (int) == 1:
            print("1")
            '''callsNewton'''
        elif selected (int) == 2:
            '''Calls Interpolated'''
            print("2")
        pass

    def regresar(self):
        pass


root = tk.Tk()
app = InterfazNewton(root)
root.mainloop()
