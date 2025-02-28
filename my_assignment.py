##Write a Python program to take two integer inputs from the user 
## and print their sum, difference, product, and quotient.

num1=int(input('write your number '))
num2=int(input('write another number here '))
sum_number= num1 + num2
multiply_number= num1*num2
difference_number= num1-num2
if num2 !=0:
    quotient = num1/num2
else:
    quotient= 'cannot be divided by zero'
print(f'sum: {sum_number}')
print(f'prduct: {multiply_number}')
print(f'difference: {difference_number}')
print(f'quotient: {quotient}')

##Given the list:numbers = [10, 20, 30, 40, 50]
##Write a Python statement to print the second and last elements of the list.   

numbers=[10, 20,30,40,50]

print(f'{numbers [1]} , {numbers [-1]}')

##* Given the list:
# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# Write a Python statement to print the first three elements using slicing.

fruits= ["apple", "banana", "cherry", "date", "fig", "grape"]

print(fruits [:3])
