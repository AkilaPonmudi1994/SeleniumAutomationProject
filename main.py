first_number = int(input("the first number is:"))
second_number =int( input("the second number is:"))

def adding_numbers():
    sum_of_two_numbers = int(first_number) + int(second_number)
    return sum_of_two_numbers

def print_calculation():
    sum_of_two_numbers = adding_numbers()
    print(sum_of_two_numbers)
    #if sum_of_two_numbers > 0:
        #print('sum gte 0')
        #return "sum is greater than 0"
    #elif sum_of_two_numbers == 0:
       # return "you have entered a zero, it won't make any sense"
    if first_number < 0:
        print("First number is:", first_number)
        return "you have entered a negative value and the value are:", first_number
    elif second_number < 0:
        print("Second number is:", second_number)
        return "you have entered a negative value and the value are:", second_number
    else :
        #print(sum_of_two_numbers)
        return "sum of 2 numbers are:", sum_of_two_numbers

x_sum1 = print_calculation()
print(x_sum1)

