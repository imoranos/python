def arithmetic_arranger(problems, show_answers=False):
    numberL = []
    
    for i in problems:
        for k in i:
            
            if k == '+' or k == '-':
                opera = k 
                break
            else:
                numberL.append(k)
               
    print(numberL)
    print(opera)
    numberL = []
    numberR = []
     

    return

print(f'\n{arithmetic_arranger(["32 + 698"])}')

# ghan9sam l3amaliya naghd ra9m lwlani nhto f varibl otani f variable o l3alama f variable 
#
#
#
#