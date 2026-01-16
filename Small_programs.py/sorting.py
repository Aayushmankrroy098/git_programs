n=int(input("How many students? = "))
names = []
for i in range (1,n+1):
    name = input(f"name {i} = ")
    names.append(name)
print(f"Original list is = {names}")
names.sort()
for i in range(0,len(names)):
    print(f"{i+1}. {names[i]}")