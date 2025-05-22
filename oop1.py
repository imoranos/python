class employee:
    employee_num = 0
    @classmethod 
    def employee_number(cls):
        print("employee count = :", cls.employee_num)
    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        employee.employee_num +=1

    def totalSalary(self,target):
        totsalary = self.salary + target
        print("total  :" ,totsalary)

    def printall(self):
        print("name   :" ,self.name)
        print("gender :" ,self.age)
        print("age    :" ,self.gender)
        print("salary :" ,self.salary)
    @staticmethod
    def information():
        print("1...................")
        print("1...................")
        print("1...................")

em1 = employee("ahmed",25,"male",2500)
em1.printall()
em1.totalSalary(1000)

em2 = employee("mohamed",30,"male",3000)
em2.printall()
em2.totalSalary(1500)

employee.employee_number()
employee.information()
