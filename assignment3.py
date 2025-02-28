import random
user_guess=random.randint(1,20)
def game():
    num_guess=0
    while True:             
            user_input=int(input('type a number between 1 and 20 '))
            num_guess=num_guess+1
            if user_input<1 or user_input>20:
                print(f"out of range put another number")
            elif user_input<user_guess:
                print("too low")
            elif user_input>user_guess:
                print("too high")
            else:
                print(f"congratulations you guessed correct in {num_guess} attempt")
                break
game()

#2. Write a function default_dict() that returns a dictionary containing some sample key-value pairs.

def default_dict():
    class_record={"primary 5":23, "primary 6":42, "primary 4":30, "primary 3":28, "primary 2":80}
    for i,j in class_record.items():
        print (f'{i}, {j}') 
default_dict()


#3 Write a function get_even_numbers() that returns a list of even numbers from 2 to 10.
def even_numbers():
    num=(2,11)
    for i in range (2,11,2):
        print(i)
even_numbers()

#4 Print Multiplication Table of a Number:
#Take an integer input and use a for loop to print its multiplication table up to 10.

num=int(input("type a number to get the multiplication table _______"))  # takes an input

for i in range (1,11): # takes the range of the number from 1-10
    print(f"{num}*{i}= {num *i}") # the {num}*{i} will multiply the number but with the= {num *i} will give the result 

#5 Reverse a String
#Take a string input and use a for loop to print it in reverse order.

word=input("type the world u want to miro_____")
miro=" "
for i in word:
    miro= i + miro
print(f"this is the miro of the world u typed: {miro}")