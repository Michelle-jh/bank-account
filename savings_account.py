from BankAccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, customer_name,current_balance, minimum_balance, account_num, routing_num, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_num, routing_num)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_earned = self.current_balance * self.interest_rate
        self.current_balance += interest_earned
        print(f"Interest Applied: ${interest_earned:.2f}\nNew Balance: ${self.current_balance:.2f}")
