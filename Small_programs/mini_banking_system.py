def deposit(balance, amount):
    balance += amount
    return balance


def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance!")
        return balance
    else:
        balance -= amount
        return balance


def show_balance(balance):
    return balance


# -------- MAIN PROGRAM --------
balance = int(input("Enter initial balance: "))

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = int(input("Enter deposit amount: "))
        balance = deposit(balance, amt)

    elif choice == 2:
        amt = int(input("Enter withdrawal amount: "))
        balance = withdraw(balance, amt)

    elif choice == 3:
        print("Current Balance:", show_balance(balance))

    elif choice == 4:
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice!")
