from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, customer_name,current_balance, minimum_balance, account_num, routing_num, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_num, routing_num)
        self.transfer_limit = transfer_limit


    def transfer(self, amount, recipient_account):
        if amount > self.transfer_limit:
            print(f"Transfer Denied: ${amount:.2f} exceeds transfer limit of ${self.transfer_limit:.2f}")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer Denied: would fall below minimum balance")
        else:
            self.current_balance -= amount
            recipient_account.current_balance += amount
            print(f"Transfer Successful: ${amount:.2f} to {recipient_account.customer_name}")
