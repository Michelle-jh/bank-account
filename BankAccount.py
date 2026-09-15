class BankAccount:
    #class attribute
    bank_title = "Python Bank"

    #construct method
    def __init__(self,customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    # methods
    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited ${amount:.2f}\nNew Balance: ${self.current_balance:.2f}")

    def withdraw(self, amount):
        #error validation
        if self.current_balance - amount < self.minimum_balance:
            print("USER IS UNABLE TO WITHDRAW BECAUSE IS BALANCE LESS THAN MINIMUM BALANCE")
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount:.2f}\nNew Balance: ${self.current_balance:.2f}")
    #method for customer information
    def print_customer_information(self):
        print("")
        print(f"Bank Name: {self.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance:.2f}")
        print(f"Minimum Balance: {self.minimum_balance:.2f}")

    #2 instances
acc1 = BankAccount("Michelle Jhonson", 500, 50)
acc1.deposit(100)
acc1.withdraw(50)
acc1.print_customer_information()

print("")

acc2 = BankAccount("Michael Anderson",200, 100)
acc2.deposit(50)
acc2.withdraw(200)
acc2.print_customer_information()