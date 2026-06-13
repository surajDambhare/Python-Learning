# While Loop
# The while loop keeps running as long as a condition is True. You use it when you don't know how many times you'll need to repeat.

from xxlimited import new


# count = 1;

# while count <= 10:
#     print(count)
#     count += 1


# Q1 Separate each digit of a number and print on a new line.
# Input: 1234
# Output: 4 → 3 → 2 → 1

# n = int(input("Enter a number : "))

# while n > 0:
#     lastDigit = n % 10    #it will give us the last digit of the number
#     print(lastDigit)
#     n //= 10  #it will remove the last digit from the number

#Q2 Accept a number and print its reverse.
# Input: 12345
# Output: 54321

# n = int(input("Enter a number : "))
# reverse = 0


# while n > 0:
#     lastDigit = n % 10;
#     reverse = reverse * 10 + lastDigit;
#     n //= 10;

# print(reverse);


# Q3 Check if a number is palindromic (equal to its reverse)
n = int(input("Enter a number : "))

original = n

reverse = 0

while(n > 0):
    lastDigit = n % 10
    reverse = reverse * 10 + lastDigit
    n //= 10

if original == reverse:
    print(f"{original} is a palindrome!")
else:
    print(f"{original} is not a palindrome!")


