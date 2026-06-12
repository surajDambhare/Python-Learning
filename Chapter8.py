#The range() Function
#range() generates a sequence of numbers. Think of it as saying "count from here to there".

#range(stop)             # 0 up to stop-1
# range(start, stop)      # start up to stop-1
# range(start, stop, step)# start, jumping by step

range(10) # 0 to 9
range(1, 10) # 1 to 9
range(1, 10, 2) # 1, 3, 5


# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(1, 10, 2)))

# for i in range(50):
#     print(i);

# n = int(input("Enter a number : "))
# for i in range(n, n*10+1, n):
#     print(i)


a = "Students"

# for i in range(len(a)):
#     print(f"{i} : {a[i]}")


# # break, continue & else — The Traffic Light Analogy
# for i in range(1, 11):
#     if i == 12:
#         break
#     if i == 3:
#         continue
#     print(f"Signal {i} : Green Light - Passed")
# else:
#     print("All Signals Passed - No Break Encountered")


# Q1 Print "Hello World" n times.
# n = int(input("Enter a number : "))

# for i in range(n):
#     print("Hello World")


# # Q2 Print the first n natural numbers.
# n = int(input("Enter a number : "))

# for i in range(1, n+1):
#     print(i);


# # Q3 Reverse for loop — print n down to 1.
# n = int(input("Enter a number : "))

# for i in range(n, 0, -1):
#     print(i);

# #Q4 Print the multiplication table of a number.

# n = int(input("Enter a number : "))

# for i in range(n, n*10+1, n):
#     print(i);

# Q5 Sum of first n natural numbers.
n = int(input("Enter a number : "))
sum = 0;

for i in range(1, n+1):
    sum += i;
print(sum);