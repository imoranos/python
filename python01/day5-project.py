def arithmetic_arranger(problems, show_answers=True):
    
    len1 = len(problems)
    if len1 >5:
        return 'Error: Too many problems.'
    list1 = []
    list2 = []
    list3 = []
    total = []
    for i in problems:
        element = i.split() #['32', '+', '698']  ['3801', '-', '2']
        if len(element[0]) > 4 or len(element[0]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        if element[0].isdigit() and element[2].isdigit():
            list1.append(element[0])
            list3.append(element[2])
        else:
            return 'Error: Numbers must only contain digits.'

        if element[1] == '+' or element[1] == '-':
            list2.append(element[1])
        else:
            return "Error: Operator must be '+' or '-'."
            
        if element[1] == '+':
            total.append(int(element[0])+int(element[2]))
        elif element[1] == '-':
            total.append(int(element[0]) - int(element[2]))
     
    for i in range(len1):
        print(list1[i].rjust(max(len(list1[i]),len(list3[i])) + 2),'  ', end=' ')
         
    print('')
    for i in range(len1):    
        print(list2[i], list3[i].rjust(max(len(list1[i]),len(list3[i]))),'  ', end=' ')
    print('')    
    for i in range(len1):
        print('-' * (max(len(list1[i]),len(list3[i])) + 2),'  ', end=' ')
    print('')
    if show_answers :
        for i in range(len1):
            print(str(total[i]).rjust(max(len(list1[i]),len(list3[i])) + 2),'  ', end=' ')

    return 

print(f'\n{arithmetic_arranger(["32 + 68", "3801 - 2", "45 + 43", "13 + 49"])}')


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