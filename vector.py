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
        return self.__class__(**kwargs)    
    
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        
        elif type(self) == type(other): 
            # args = [1,2,3,4,] -> sum(args) -> 1+2+3+4 ..
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented
    
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other
        
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        
        return self.__class__(**kwargs)    

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

#final step
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

# dict = {'x': 2 ,'y': 3}
# dict["x"]
# vars(self) -> {'x': 2 ,'y': 3}   i = 'x': 2
