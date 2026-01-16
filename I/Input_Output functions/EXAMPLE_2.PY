x,y,z = map(int, input("Enter any three numbers separated by space only : ").split())
sum = x+y+z
product = x*y*z
average = sum/3
print(f"\nsum = {sum}\n product = {product}\n average = {average}")
if x>y & x>z :
    print("\nX is the greatest.")
elif y>z:
     print("\nY is the greatest.")
else :
      print("\nZ is the greatest.")