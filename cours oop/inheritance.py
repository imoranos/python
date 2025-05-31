class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printAll(self):
        print(self.name, self.age ,self.gender)

# had lklas wart khasaeis man lclas Person 
class Employee(Person):
    def __init__(self, name, age, gender, salary):
        Person.__init__(self, name, age, gender)
        self.salary = salary
    def printAll(self):
        print(self.name, self.age ,self.gender, self.salary)

class Manager:
    def __init__(self,name,id , location):
        self.name = name
        self.id = id
        self.location = location

    def printAll(self):
        print(self.name,self.id , self.location)

class Ceo(Employee,Manager):
    def __init__(self, name, id, location, age, gender, salary):
        Manager.__init__(self, name, id, location)
        Employee.__init__(self,name, age, gender, salary)
    
    def printAll(self):
        print(self.name, self.age ,self.gender, self.salary,self.id, self.location)

emp1 = Employee("ahmed", 25, "male", 2500)
emp1.printAll()


Ceo1 = Ceo("mohamed", 1,"egypt", 40,"male", 10000)
Ceo1.printAll()

