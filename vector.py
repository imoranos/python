class R2Vector:

    # attribute --------------------------------
    def __init__(self, *, x, y):
        self.x = x
        self.y = y
    # methods ----------------------------------
    def norm(self):
        #return (self.x**2 + self.y**2)**0.5    step 1
        #return sum(val**2 for val in self.__dict__.values())**0.5  step 2
        return sum(val**2 for val in vars(self).values())**0.5
    
    def __str__(self):
        #return f'{self.x, self.y}'  step 1 return just 2 x and y
        return str(tuple(getattr(self, i) for i in vars(self)))
    
    def __repr__(self):
        arg_list = [ f'{key}={val}' for key,val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    #def __getattribute__(self,attr):
        #return 'calling __getattribute__'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return kwargs    

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
         


# object ---------------------------
v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)
print(v1.norm())
print(v2.norm())

print(f'v1 = {v1}')
print(f'v2 = {v2}')

v3 = R2Vector(x=5, y=10)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(v1.__add__(v3))

# dict = {'x': 2 ,'y': 3}
# dict["x"]
# vars(self) -> {'x': 2 ,'y': 3}   i = 'x': 2
