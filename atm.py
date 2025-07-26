balance = 10000

def check_balance():
    print(f"\nYour current balance is ₦{balance}\n")

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: ₦"))
    if amount > 0:
        balance += amount
        print(f"₦{amount} deposited successfully.\n")
    else:
        print("Invalid amount.\n")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: ₦"))
    if 0 < amount <= balance:
        balance -= amount
        print(f"₦{amount} withdrawn successfully.\n")
    else:
        print("Insufficient funds or invalid amount.\n")

while True:
    print("Welcome to ATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else: 
        print("Invalid choice. Please try again.\n")