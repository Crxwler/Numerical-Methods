

class Newton:
    iteration = list()
    x_n = list()
    f_x_n = list()
    derivate = list()
    val_abs = list()
    error = list()

    def __init__(self):
        super().__init__()

    def newton(self, fun, derivative, x0, criteria, max_iter):
        '''Approximate solution of f(x)=0 by Newton's method.

        Parameters
        ----------
        fun : function
            Function for which we are searching for a solution f(x)=0.
        derivative : function
            Derivative of f(x).
        x0 : number
            Initial guess for a solution f(x)=0.
        criteria : number
            Stopping criteria is abs(f(x)) < criteria.
        max_iter : integer
            Maximum number of iterations of Newton's method.

        Returns
        -------
        xn : number
            Implement Newton's method: compute the linear approximation
            of f(x) at xn and find x intercept by the formula
                x = xn - f(xn)/derivative(xn)
            Continue until abs(f(xn)) < criteria and return xn.
            If derivative(xn) == 0, return None. If the number of iterations
            exceeds max_iter, then return None.
        '''

        xn = x0
        for n in range(0, max_iter):
            self.iteration.append(n)
            fxn = fun(xn)
            self.f_x_n.append(fxn)
            self.val_abs.append(abs(fxn))
            if abs(fxn) < criteria:
                self.x_n.append(xn)
                return xn
            derivativexn = derivative(xn)
            self.derivative.append(derivativexn)
            if derivativexn == 0:
                return None
            old = xn
            xn = xn - fxn / derivativexn
            self.error.append( abs((xn - old)/xn))
            self.x_n.append(xn)
        return None

