def check(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")
for i in range(6):
    x = int(input("Enter a number: "))   
    check(x)