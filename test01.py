def arithmetic_arranger(problems, show_answers=False):

    len1 = len(problems)
    if len1 >5:
        return 'Error: Too many problems.'
    line1 = ''
    line2 = ''
    line3 = ''
    total = ''
    for i in problems:
        element = i.split() #['32', '+', '698']  ['3801', '-', '2']
        number1 = element[0]
        operator = element[1]
        number2 = element[2]

        if len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        withe = (max(len(number1) ,len(number2)) + 2)
        if number1.isdigit() and number2.isdigit():
            line1 += (number1.rjust(withe ) + '    ') 
            line2 += (operator + number2.rjust(withe - 1) + '    ')
        else:
            return 'Error: Numbers must only contain digits.'
    
        if operator == '+' or operator == '-':
            line3 += ('-' * withe + '    ')
        else:
            return "Error: Operator must be '+' or '-'."
        
        if operator == '+':
            to = int(number1) + int(number2)
            total += (str(to).rjust(withe ) + '    ') 
        elif operator == '-':
            to = int(number1) - int(number2)
            total += (str(to).rjust(withe ) + '    ')
       
    line1 = line1[:-4]
    line2 = line2[:-4]
    line3 = line3[:-4]
    total = total[:-4]
    if not show_answers:
        return line1 + "\n" + line2 + "\n" + line3
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + total
    
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')


#"apple orange".split() → ['apple', 'orange']
# ghan9sam l3amaliya naghd ra9m lwlani nhto f varibl otani f variable o l3alama f variable 
#first number
#operater
#second number
#gad function dyal total
#gad function likathwl list l int 
#print(" ".join(a))
# condition 1 : >= 5 problem ---> Valid
# condition 2 : operator == + or - ---> Valid
# condition 3 : just have a digit in number no char  ---> Valid
# condition 4 : max digit in number is 4""""