import tkinter as tk
from tkinter import ttk, CENTER
#import sympy as sy
import newton


class InterfazNewton:
    # indice
    z = 0

    def __init__(self, master):
        self.text = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        self.master = master
        master.title("Newton")
        master.geometry("1100x400")
        # Crear caja de texto.
        # Expresion.
        self.label = tk.Label(master, text="introduzca la expresion")
        self.label.place(x=50, y=20)
        self.entry = ttk.Entry(master, textvariable=self.text)
        self.entry.place(x=50, y=50)
        # Datos de X0
        self.label2 = tk.Label(root, text="El valor de x(0)")
        self.label2.place(x=200, y=20)
        self.entry2 = ttk.Entry(master, textvariable=self.text2)
        self.entry2.place(x=200, y=50)
        # Datos de la cantidad de resultados
        self.label3 = tk.Label(master, text="cantidad de veces")
        self.label3.place(x=350, y=20)
        self.entry3 = ttk.Entry(master, textvariable=self.text3)
        self.entry3.place(x=350, y=50)
        # Datos del numero maximo
        self.label4 = tk.Label(master, text="hasta que numero")
        self.label4.place(x=500, y=20)
        self.entry4 = ttk.Entry(master, textvariable=self.text4)
        self.entry4.place(x=500, y=50)
        # Botones
        self.button = tk.Button(root, text="Regresar", command=self.Regresar)
        self.button.place(x=50, y=80)
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
        # print("Calculate")
        data = self.text.get()
        data2 = self.text2.get()
        data3 = self.text3.get()
        data4 = self.text4.get()
        symbols = {'x', sy.Symbol('x', real=True), 'y', sy.Symbol('y', real=True)}
        #fun = sy.parse_expr(data2, symbols)
        #diff = sy.diff(fun, symbols['x'])
        ##fun = sy.lambdify(fun) -> not used
        obj = newton.Newton(data, lambda x: 3 * x ** 2 - 2, data2, data3, data4)

        # print(data, data2, data3)
        # print(self.text.get(), self.text2.get(), self.text3.get())
        return None

    def Regresar(self):
        return None


root = tk.Tk()
app = InterfazNewton(root)
root.mainloop()
