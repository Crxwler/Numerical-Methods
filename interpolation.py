import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate as interpolate


class Interpolation:
    y = list()
    x = list()
    a = list()
    data = None

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def compute(self, p):
        '''Interpolation

        Params:
            p - Interpolation va
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
        result = [val for val in values]
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
        result = 0
        for i in range(self.x.ndim):
            p = 1
            for j in range(self.x.ndim):
                if i != j:
                    p *= (value - self.x[j]) / (self.x[i] - self.x[j])
            result += p * self.y[i]
        return result  # interpolated value
