# # write a program to check whether the given number is between 1 to 10?
#
# n = int(input("Enter the number: "))
# is_valid = n>=1 and n<=10
#
# if is_valid:
#     print("The number", n, "is between 1 to 10")
#
# else:
#     print("not met the expectation")
#     print(n>=1 and n<=10)


# Print numbers from 1 to 10 by using while loop

# i = int(input("Enter the number:"))
# i=0 #initialization
# while i<=10: #condition
#     print(i)
#     i=i+1 #increment

# Print numbers from 10 to 1 by using while loop
#
# i = 10  # initialization
# while i >= 0:  # condition
#     print(i)
#     i = i - 1  # increment


# To display sum of first n numbers

# n = int(input("Enter the number : "))
# sum = 0
# i = 1
# while i <= n:
#   sum = sum + i
#   i = i + 1
#   print("The sum of first" , n , "number is : ", sum)

# write a program to prompt user to enter some name until entering shankar

#name =''
# while name != 'shankar':
#     name = input("Enter name :")
# print("Thanks you " , name)

#With arguments and no return value

def my_fun(name):
    print("Hello", name)


s=my_fun("Akila")
print(s)
my_fun("Mohan")