class employee():
    def __init__(self, name, age ,  gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary= salary
    


    def salaryNet(self,tax):
        
        self.salary = int(self.salary - self.salary*tax)
        #print("salary net : ",salarynet)


    def printall(self):
        print(self.name, self.age, self.gender, self.salary)

    

worker1 =employee("khalid", 31 , "male", 3500)

worker1.salaryNet(0.14)
worker1.printall()
#worker1.salaryNet(0.14)


