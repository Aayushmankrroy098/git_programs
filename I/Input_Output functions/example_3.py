''' marks = [60, 70, 80, 90]
for m in marks:
    print(m)
word = "Python"
for ch in word:
    print(ch)
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
num = -1
while num < 0: # Keeps asking input until the user gives a correct value.
    num = int(input("Enter a positive number: ")) '''

# choice = 0
# while choice != 3:
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Exit")
#     choice = int(input("Enter choice: "))

# n = int(input("Enter number (-1 to stop): "))
# while n != -1:
#     print(n)
#     n = int(input("Enter number (-1 to stop): "))

# sum=0
# n = 123
# while n > 0:
#     print(n % 10)
#     sum += (n%10)
#     n //= 10
# print(sum)


# while True:
#     print("Running...")

# Linear search using while loop

# lst = [10, 25, 30, 45, 60]
# key = int(input("Enter element to search: "))

# i = 0


# while i < len(lst):
#     if lst[i] == key:
#         found = True
#         break
#     i += 1

# if found:
#     print("Element found at index", i)
# else:
#     print("Element not found")

squares = [x*x for x in range(5)]
print(squares)