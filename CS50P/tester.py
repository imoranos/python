
#hello1.y -------------------------------------------
"""# ask user for their name


name = input("what's your name?: ")

#remove whitespace from str
name = name.strip().title()

#say hello to user 
print(f"hello, {name}")
 
"""
#----------------------------------------------------
#calculator1.py---------------------------------------
"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z =  x / y  

print(f'{z:^25.2f}')

"""
#----------------------------------------------------
#hello2.y --------------------------------------------
"""
def main():
    name = input("what's your name?: ")
    hello(name)

def hello(to = "world"):
    print("hello,",to)

main()
"""
#----------------------------------------------------
#calculator1.py---------------------------------------
def main():
    x = int(input("what's x?: "))
    print('x square is',square(x))

def square(n):
    return pow(n,2)  # pow(n,2)
main()

#----------------------------------------------------
"""
variables
comment 
pseducode
print(parametrs , end = ,sep= )
.strip()  -> remove whitespace from str
.capitalize()  khalid ait alla ->Khalid ait alla
.title() khalid ait alla -> Khalid Ait Alla
l strip and l strip 
operators + - * / ....
interactive mode
data type int float round(x / y , 3)-> .3n  or :.2f  
functions -> def 
scop  / return / pow(n,2) --> n**2

"""