# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import seaborn as sns


# # cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))


# # casting from int to str
# # integer = 12345
# # integer_to_str = str(integer)
# # print("Before casting :", integer, ", the data type is", type(integer))
# # print("After casting :", integer_to_str, ", the data type is",
# # type(integer_to_str))


# # casting from int to bool
# # num_int = 1
# # num_bool = bool(num_int)
# # print(num_bool, type(num_bool))
# # num_int = 0
# # num_bool = bool(num_int)
# # print(num_bool, type(num_bool))


# # Equal to
# print(8 == 8)
# # Not equal to
# print(8 != 9)
# # Greater than
# print(8 > 9)
# # Less than
# print(8 < 9)
# # Less than
# print(8 <= 9)
# # Less than
# print(9 >= 9)


# # a = True
# # b = True
# # print(a and b)
# # print(a or b)
# # print(not b)
# # #logic
# # 5 > 6 and 6 < 7


# # e = 8
# # f = 2
# # # Summation
# # sum = e + f
# # print(f"The sum of e with f is : {sum}\n")
# # # Reduction
# # red = e - f
# # print(f"The reduction of e with f is : {red}\n")

# # # Multiplication
# # multi = e * f
# # print(f"The multipication of e with f is : {multi}\n")
# # # Division
# # divi = e / f
# # print(f"The quotient of e with f is : {divi}\n")
# # # Modulo
# # mod = e % f
# # print(f"The remainder of e with f is : {mod}\n")
# # # Power
# # pow = e ** f
# # print(f"The power of e of f is : {pow}\n")


# # name = str(input("What is your name : "))
# # age = int(input("What's your age : "))
# # # print("Name: ", name)
# # # print("Age: ", age)


# # # normal print
# # print('Hi all! I am', name, 'age', age, 'years old')
# # # Hi all! I am Parman age 24 years old
# # # format print
# # print(f'Hi all! I am {name} age {age} years old')
# # # Hi all! I am Parman age 24 years old
# # # format print
# # print(f'Hi all! I am %s age %d years old'%(name, age))
# # # fortmat output
# # print(30*"=")
# # print("Temperature Calculator Program")
# # print(30*"=")


# try:
#     your_GPA = float(input("Enter your GPA: "))
#     if 4.0 >= your_GPA >= 0.0:
#         if 4.0 >= your_GPA >= 3.80:
#             print(f"Damn you've got a magna cumlaude with your {your_GPA}GPA")
#         elif 3.50 <= your_GPA < 3.80:
#             print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
#         elif 3.00 <= your_GPA < 3.50:
#             print(f"You've got a stable GPA tho")
#         elif your_GPA < 3.0:
#             print(f"You need a stable GPA")
#     else:
#         print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
# except:
#     print("Please enter a valid GPA")

n = 0
while n < 3:
    print("Nilai n =", n)
    n += 1
