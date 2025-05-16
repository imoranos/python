def arithmetic_arranger(problems, show_answers=False):
    number1 = []
    operater = []
    number2 = []
    for i in problems:
        if i.find('-') >= 1:
            index_oper = i.find('-')
            oper = i[index_oper]
        elif i.find('+') >= 1:
            index_oper = i.find('+')
            oper = i[index_oper]
        else:
            print('operator not found')
            break
        counter = 0
        print(index_oper)
        print(oper)
        for k in i:
            #"32 + 698"
            #"32 + 698", "3801 - 2", "45 + 43", "123 + 49"
            #"apple orange".split() → ['apple', 'orange']
            if counter < index_oper and k != ' ':
                
                number1.append(k)
            
            if counter > index_oper and k != ' ':
                number2.append(k)
            counter +=1

            #number1.append(k)
        print(number1)
        print(number2)
        number1 = int(''.join(map(str, number1)))
        number2 = int(''.join(map(str, number2)))
        print(number1)
        print(oper)
        print(number2)
        if oper == '+':
            total = number1 + number2
        elif oper == '-':
            total = number1 - number2
        print(f'total: {total}')    
    return


def main():
    arithmetic_arranger(["32 + 698"])
main()
# ghan9sam l3amaliya naghd ra9m lwlani nhto f varibl otani f variable o l3alama f variable 
#first number
#operater
#second number
#gad function dyal total
#gad function likathwl list l int 