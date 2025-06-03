from abc import ABC , abstractmethod
class Equation(ABC):

    degree: int
    def __init__(self, *args):
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        
        """for arg in args:
            if not isinstance(arg,(int,float)):
                raise TypeError("Coefficients must be of type 'int' or 'float'")"""
        # change for by any ------ isinstance() ---cheking if args is float or int 
        if any(not isinstance(arg,(int,float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        
        #if LinearEquation(a,b) >> a = 0  cheking if first args nit equal 0
        if args[0] == 0:
            raise ValueError('Highest degree coefficient must be different from zero')

        # use enumerate . build dictionary {1:2 , 0:3}
        self.coefficients = {self.degree - i: cof for i,cof in enumerate(args)}

        #LinearEquation(2,3,5) -> 2x**2 + 3x + 5

    def __init_subclass__(cls):
        #lbaht f child wax fih degree
        if not hasattr(cls,"degree"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")
    
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x') 
            else:
                terms.append(f'{coefficient:+}x**{n}')               
        equation_string = ' '.join(terms) + ' = 0'
        return equation_string.strip('+')  

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod    
    def analyze(self):
        pass
        

class LinearEquation(Equation):
    degree = 1
    def solve(self):
        a, b =self.coefficients.values() # {1:2 , 0:3}  a = 2 , b = 3
        # 2x +3 = 0
        x = -b/a
        return x
    
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}

class QuadraticEquation(Equation):
    degree = 2
    
    def __init__(self, *args):
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c
    
    def solve(self):
        pass

      
    def analyze(self):
        pass


#eq = Equation()
lin_eq = LinearEquation(2,3)
print(lin_eq)
print(lin_eq.solve())
print(lin_eq.analyze())
quadr_eq = QuadraticEquation(11, -1, 1)
print(quadr_eq)

""" 
test = (5,3)
a , b =  test

"""
