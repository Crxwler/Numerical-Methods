
class Newton:

    def __init__(self) -> None:
        super().__init__()

    def newton(f, Df, x0, epsilon, max_iter):
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

        Examples
        --------
        >>> f = lambda x: x**2 - x - 1
        >>> Df = lambda x: 2*x - 1
        >>> newton(f,Df,1,1e-8,10)
        Found solution after 5 iterations.
        1.618033988749989
        '''
        xn = x0
        for n in range(0, max_iter):
            print('Iteration :', n)
            fxn = f(xn)
            print('Initial fxn', fxn)
            if abs(fxn) < epsilon:
                print('Found solution after', n, 'iterations.')
                print('Value of xn :',xn);
                return xn
            Dfxn = Df(xn)
            print('value of dfxn', Dfxn)
            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn / Dfxn
            print('value 2 of xn', xn)
        print('Exceeded maximum iterations. No solution found.')
        return None



f = lambda x: x ** 3 - 2 * x - 5
Df = lambda x: 3 * x ** 2 - 2
val = Newton.newton(f, Df, 1, 1e-8, 10)
# print(" {0:.10f} ".format(val))
print(val)
