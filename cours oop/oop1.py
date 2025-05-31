class employee:
    # ttribuats
    number_of_employee = 0
     
    # class method
    @classmethod
    def employeeNum(cls):
        print("employee count = : ", cls.number_of_employee)

    # insta,ce method 
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        employee.number_of_employee +=1
    # methods ----------------------------------------------   
    def totalSalary(self,target):
        totsalary = self.salary + target
        print("total salary :",totsalary)
        print('-------------------------------\n')

    def printAll(self):
        print("name :",self.name,"age :",self.age,"gender :",self.gender,"salary :",self.salary)
    
    # static method
    @staticmethod
    def information():
        print(" 1- learn dev. \n 2- learn germany languge.\n 3- learn english languge.")

#object

em1 = employee("ahmed",25,"male", 2500)
em1.printAll()
em1.totalSalary(1000)

em2 = employee("mohamed",30,"male", 3000)
em2.printAll()
em2.totalSalary(1500)

#call class method 
employee.employeeNum()

#call static method
employee.information()
