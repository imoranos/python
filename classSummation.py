class Summation:
    def sum(datatype, *args):
        if datatype == 'int':
            count = 0
        if datatype == 'str':
            count = ''

        for x in args:
            count = count + x
        print("total = ", count)

sum1 = Summation
sum1.sum('int', 1, 2, 3)
sum1.sum('str', "khalid ", "ait alla")