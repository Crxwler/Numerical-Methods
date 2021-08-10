import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate as interpolate
import sympy


class Interpolation:
    y = list()
    x = list()
    a = list()
    data = None

    def __init__(self, x, y):
        super().__init__()
        self.x = [float(i) for i in x]
        self.y = [float(i) for i in y]

    def compute(self, p):
        '''Interpolation

        Params:
            p - Interpolation value
        Returns:
            result - Interpolated value
        '''

        values = []
        for i in range(len(self.a)):
            mult = 1
            for j in range(len(self.a)):
                if i == j:
                    continue
                mult = (p - self.x[j]) * mult
            values[i] = self.a[i] * mult
        result = sum(values)
        return result

    def plotInitialData(self):
        self.data = pd.DataFrame({'x': self.x, 'y': self.y})
        plt.fig(figsize=(12, 10))
        plt.scatter(self.data.x, self.data.y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def plotData(self):
        linear = interpolate.lagrange(self.data.x, self.data.y)
        plt.fig(figsize=(12, 10))
        plt.scatter(self.data.x, self.data.y, linear)
        plt.xlim(0, 7)
        plt.ylim(0, 50)
        plt.title('Lagrange')
        plt.show()

    def compute2(self, value):
        '''Interpolation

            Params:
                value - value to be interpolated
            Returns:
                result - Interpolated value
        '''
        value = float(value)
        result = 0
        for i in range(len(self.x)):
            p = 1
            for j in range(len(self.x)):
                if i != j:
                    p *= (value - self.x[j]) / (self.x[i] - self.x[j])
            result += p * self.y[i]
        return result  # interpolated value

    def compute3(self, value):
        x = np.array(self.x)
        y = np.array(self.y)
        n = len(x)
        x1 = sympy.Symbol('x')
        val = 0
        div = np.zeros(n, dtype = float)
        for i in range(0, n, 1):
            result = 1
            de = 1
            for j in range(0, n, 1):
                if i != j :
                    result *= (x1-x[j])
                    de *= (x[i]-x[j])
            term= result/de
            val += term*y[i]
            div[i] = de
        simple = val.expand()
        px = sympy.lambdify(x1, simple)
        m = 100
        a = np.min(x)
        b = np.min(y)
        pxi = np.linspace(a, b, m)
        pfi = px(pxi)
        plt.plot(x, y, 'o', label = 'Points')
        plt.plot(pxi, pfi, label = 'Polynomials')
        plt.legend()
        plt.xlabel("xi")
        plt.ylabel("fi")
        plt.title("Interpolation of lagrange")
        plt.show()