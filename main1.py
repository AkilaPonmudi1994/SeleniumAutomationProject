input1 = int(input('enter number 1: '))
input2 = int(input('enter number 2: '))


# funtion should do one job
# should take input
# should produce output
def add(a, b):
    _sum1 = a + b
    return _sum1
def validate_input(x):
    if x > 0:
        return 'yes'
    else:
        return 'no'
if validate_input(input1) == 'yes' and validate_input(input2) == 'yes' :
    _sum1 = add(input1,input2)
    print (_sum1)
else :
    if validate_input(input1) != 'yes' :
        print( 'invalid i1 input', input1)
    if validate_input(input2) != 'yes' :
        print('invalid i2 input', input2)




