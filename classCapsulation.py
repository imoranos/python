class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def setmanagersalary(self,obj,newsalary):
        obj.salary =  newsalary

class Manager:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
    def getmanagersalary(self,obj):
        print(obj._salary)

class Ceo(Manager):
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def setmanagersalary(self,obj,newsalary):
        obj._salary = newsalary

    def setceosalary(self,obj,newsalary):
        obj.__salary = newsalary

    def getceosalary(self,obj):
        print(obj.__salary)    

emp1 = Employee("ahmed",2000)
mng1 = Manager("mohmed",3000)

emp1.setmanagersalary(mng1,4000)
mng1.getmanagersalary(mng1)
ceo1 = Ceo("khaled",5000)
ceo1.setmanagersalary(mng1,4500)
mng1.getmanagersalary(mng1)
ceo1.getmanagersalary(mng1)
ceo1.getceosalary(ceo1)
ceo1.setceosalary(ceo1,6000)
ceo1.getceosalary(ceo1)

