from tkinter.ttk import Treeview
import sympy as sy

import interpolation
from Newton import Newton

try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Matematicas para Ingenieria - II")
        self.geometry("600x400")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Menu, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Interpolation",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Newton",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):
    #coordenadas
    x = list()
    y = list()
    #indice
    z = 0

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Interpolation of Lagrange", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()
        self.message = tk.StringVar(value="Resultado    :")
        self.text = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        # Datos de x
        self.label = tk.Label(self, text="X")
        self.label.place(x=50, y=70)
        self.entry = tk.Entry(self, textvariable=self.text)
        self.entry.place(x=50, y=100, width=20, height=20)
        # Datos de y
        self.label2 = tk.Label(self, text="Y")
        self.label2.place(x=80, y=70)
        self.entry2 = tk.Entry(self, textvariable=self.text2)
        self.entry2.place(x=80, y=100, width=20, height=20)
        # Datos del valor a evaluar
        self.label3 = tk.Label(self, text="Input")
        self.label3.place(x=130, y=70)
        self.entry3 = tk.Entry(self, textvariable=self.text3)
        self.entry3.place(x=130, y=100,  width=30, height=20)
        # Botones
        self.button = tk.Button(self, text="Agregar", command=self.agregar)
        self.button.place(x=50, y=130)
        self.button2 = tk.Button(self, text="Calcular", command=self.calcular)
        self.button2.place(x=130, y=130)
        #self.button2 = tk.Button(self, text="Regresar",
        #                        command=lambda: controller.show_frame("Menu"))
        #self.button2.place(x=350, y=80)
        # Add a Treeview widget
        self.tree = Treeview(self, column=("x", "y"),
                                 show='headings', height=5)
        self.tree.column("# 1", anchor=tk.CENTER, width=60)
        self.tree.heading("# 1", text="x")
        self.tree.column("# 2", anchor=tk.CENTER, width=60)
        self.tree.heading("# 2", text="y")
        self.tree.place(x=50, y=200)
        #Resultado
        self.label4 = tk.Label(self, text=self.message)
        self.label4.place(x=50, y=350)
        # self.place(width=1100, height=400)

    def calcular(self):
        # print("Calculate")
        data3 = self.text3.get()
        obj = interpolation.Interpolation(self.x, self.y)
        obj.plotData()
        print(obj.compute2(data3))
        return None

    def agregar(self):
        # print("ADD")
        data = self.text.get()
        data2 = self.text2.get()
        self.x.append(data)
        self.y.append(data2)
        self.z = self.z + 1
        self.tree.insert(parent='', index=self.z, iid=self.z, text='', values=(data, data2))
        # print(data, data2, data3)
        # print(self.text.get(), self.text2.get(), self.text3.get())
        return None

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Newthon Raphson", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()
        self.text = tk.StringVar()
        self.text2 = tk.StringVar()
        self.text3 = tk.StringVar()
        self.text4 = tk.StringVar()
        # Crear caja de texto.
        # Expresion.
        self.label = tk.Label(self, text="Introduzca la expresion")
        self.label.place(x=50, y=120)
        self.entry = tk.Entry(self, textvariable=self.text)
        self.entry.place(x=50, y=150)
        # Datos de X0
        self.label2 = tk.Label(self, text="x(0)")
        self.label2.place(x=200, y=120)
        self.entry2 = tk.Entry(self, textvariable=self.text2)
        self.entry2.place(x=200, y=150, width=20, height=20)
        # Datos de la cantidad de resultados
        self.label3 = tk.Label(self, text="Iteracion")
        self.label3.place(x=240, y=120)
        self.entry3 = tk.Entry(self, textvariable=self.text3)
        self.entry3.place(x=240, y=150, width=20, height=20)
        # Datos del numero maximo
        self.label4 = tk.Label(self, text="hasta que numero")
        self.label4.place(x=300, y=120)
        self.entry4 = tk.Entry(self, textvariable=self.text4)
        self.entry4.place(x=30, y=150, width=40, height=20)
        #Botones
        #self.button = tk.Button(self, text="Regresar",
        #                        command=lambda: controller.show_frame("Menu"))
        #self.button.place(x=50, y=80)
        self.button = tk.Button(self, text="Calcular", command=self.calcular)
        self.button.place(x=370, y=150)
        # Create an object of Style widget
        #self.style = tk.Style()
        #self.style.theme_use('clam')
        # Add a Treeview widget
        self.tree = Treeview(self, column=("xn", "yn", "valor real", "valor absoluto", "Error relativo"),
                                 show='headings', height=5)
        self.tree.column("# 1", anchor=tk.CENTER, width=60)
        self.tree.heading("# 1", text="xn")
        self.tree.column("# 2", anchor=tk.CENTER, width=60)
        self.tree.heading("# 2", text="yn")
        self.tree.column("# 3", anchor=tk.CENTER, width=60)
        self.tree.heading("# 3", text="valor real")
        self.tree.column("# 4", anchor=tk.CENTER, width=70)
        self.tree.heading("# 4", text="valor absoluto")
        self.tree.column("# 5", anchor=tk.CENTER, width=80)
        self.tree.heading("# 5", text="Error relativo")
        self.tree.place(x=50, y=200)

    def calcular(self):
        # print("Calculate")
        data = sy.sympify(self.text.get())
        data2 = self.text2.get()
        data3 = self.text3.get()
        data4 = self.text4.get()
        symbols = {'x', sy.Symbol('x', real=True)}
        print(data)
        fun = data
        diff = sy.diff(data, symbols['x']) #->differential
        obj=Newton()
        obj.newton(data, diff, 1, 1e-8, 10)
        # print(data, data2, data3)
        # print(self.text.get(), self.text2.get(), self.text3.get())
        return None


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()