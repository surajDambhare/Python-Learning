# #you have to take input of age and tell the 
# # person can vote or not

# age = int(input("what is your age :- "));
# if age >= 18:
#     print("Hello Brother you can vote")
# else:
#     print("Hello Brother you can't vote")


# rupees = int(input("Give Money : "))

# if rupees == 10 : 
#     print("I will have a chocobar")
# elif rupees == 20:
#     print("I will have a burger")
# elif rupees == 50:
#     print("I will have a pizza")
# else:
#     print("I will have a samosa")


# #Question 1 - Accept two numbers and print the greatest between them.
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")


# #Question 2 - Accept gender from user and print a greeting message.
# gender = input("Enter Character Either M OR F : ")

# if gender == "M" or gender == "m":
#     print("Good Morning Sir")
# elif gender == "F" or gender == "f":
#     print("Good Morning Ma'am")
# else:
#     print("Others")


# #Question 3 - Accept an integer and check if it is even or odd.
# number = int(input("Enter a number : "))

# if number % 2 == 0:
#     print(f"{number} is Even!")
# else:
#     print(f"{number} is Odd!")


# #Question 4 - Accept a year and check if it is a leap year.
# divisible by 400 → leap
# OR divisible by 4 but not by 100 → leap
year = int(input("Enter a Year : "))

#Century Here 1600 
if year % 400 == 0 and year % 100 == 0:
    print(f"{year} Leap Year")
elif year % 100 != 0 and year % 4 == 0:
    print(f"{year} Leap Year")
else:
    print(f"{year} Not Leap Year")


#Question 6 - Accept temperature in °C and print a description.
temperature = int(input("Enter The Current Temperature : "))

if temperature >= -5 and temperature <= 5:
    print("Freezing Weather")
elif temperature > 5 and temperature  <= 15:
    print("Very Cold Weather")
elif temperature > 15 and temperature <= 25:
    print("Cold Weather")
elif temperature > 25 and temperature <= 35:
    print("Hot Weather")
else:
    print("Very Hot Weather")