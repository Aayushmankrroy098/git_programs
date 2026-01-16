print("THIS IS THE CONVERTER OF USD INTO NPR")
print("According to latest update, 1 USD = Rs. 144.61")
x = int(input("Enter USD : ") )
def convert(usd):
    rs = usd*144.61
    print(x, " USD = ", "Rs. ", rs)
convert(x)