import pandas as pd

class Newton:
    iteration = list()
    x_n = list()
    f_x_n = list()
    derivate = list()
    val_abs = list()
    error = list()

    def __init__(self):
        super().__init__()

    def newton(self, f, Df, x0, epsilon, max_iter):
        '''Approximate solution of f(x)=0 by Newton's method.

        Parameters
        ----------
        f : function
            Function for which we are searching for a solution f(x)=0.
        Df : function
            Derivative of f(x).
        x0 : number
            Initial guess for a solution f(x)=0.
        epsilon : number
            Stopping criteria is abs(f(x)) < epsilon.
        max_iter : integer
            Maximum number of iterations of Newton's method.

        Returns
        -------
        xn : number
            Implement Newton's method: compute the linear approximation
            of f(x) at xn and find x intercept by the formula
                x = xn - f(xn)/Df(xn)
            Continue until abs(f(xn)) < epsilon and return xn.
            If Df(xn) == 0, return None. If the number of iterations
            exceeds max_iter, then return None.
        '''

        xn = x0
        for n in range(0, max_iter):
            print('Iteration :', n+1)
            self.iteration.append(n+1);
            fxn = f(xn)
            self.f_x_n.append(fxn)
            self.val_abs.append(abs(fxn))
            #print('Initial fxn', fxn)
            if abs(fxn) < epsilon:
                self.x_n.append(xn)
                return xn
            Dfxn = Df(xn)
            self.derivate.append(Dfxn)
            #print('value of dfxn', Dfxn)
            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            old = xn
            xn = xn - fxn / Dfxn
            self.error.append(abs(xn - old) /100)
            self.x_n.append(xn)
        print('Exceeded maximum iterations. No solution found.')
        return None


'''
f = lambda x: x ** 3 - 2 * x - 5
Df = lambda x: 3 * x ** 2 - 2
newton = Newton()
val = newton.newton(f, Df, 1, 1e-8, 10)
# print(" {0:.10f} ".format(val))
print(val)
print("Iteraion", newton.iteration)
print( "XN", newton.x_n)
print( "fxn", newton.f_x_n)
print( "abs val", newton.val_abs)
print( "f'", newton.derivate)
print( "Error", newton.error)
'''