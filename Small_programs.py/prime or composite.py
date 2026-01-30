for j in range(1,11):
    n=int(input("\nEnter any number:"))
    i=1
    count=0
    while i<=n:
            if n%i==0:
                count=count+1
            i=i+1
    if count<2:
         print(f"\nThe number {n} is neithe prime nor composite.")       
    elif count==2:
        print(f"\n The number {n} is prime.")
    else:
         print(f"\nThe number {n} is composite.")
        