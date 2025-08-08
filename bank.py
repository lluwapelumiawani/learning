class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₦{amount:.2f} to {self.name}'s account.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"Withdrew ₦{amount:.2f} from {self.name}'s account.")

    def view_balance(self):
        print(f"{self.name}'s account balance: ₦{self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                print("Account number already exists!")
                return
        new_account = BankAccount(name, account_number)
        self.accounts.append(new_account)
        print(f"Account created for {name} (Acct#: {account_number}).")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None
