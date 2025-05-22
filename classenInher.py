class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printall(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Employee(Person):
    def __init__(self,name,age, gender,salary):
        Person.__init__(self, name, age, gender)
        self.salary = salary
    
    def printall(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.salary)

emp1 = Employee("ahmed",25,"male", 2500)

emp1.printall()

class Manager:
    def __init__(self,name,id,location):
        self.name = name
        self.id = id
        self.location = location

    def printall(self):
        print(self.name)
        print(self.id)
        print(self.location)

class Ceo(Employee,Manager):
    def __init__(self, name, id, location, age, gender, salary):
        Manager.__init__(self, name, id, location)
        Employee.__init__(self, name, age, gender, salary)

    def printall(self):
        print(self.name)
        print(self.id)
        print(self.location)
        print(self.age)
        print(self.gender)
        print(self.salary)

ceo1 = Ceo("mohamad", 1,"maroc", 25, "male", 10000)
ceo1.printall()
