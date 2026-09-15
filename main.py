from checking_account import CheckingAccount
from savings_account import SavingsAccount

#scenario 1 - user1 opens checkings account, deposits money, withdraws,
# and then attempts to transfer but exceeds the limit and attempts to transfer again with a vaild one
checkAcc1 = CheckingAccount("Michelle Jhonson", 500, 50, "123123", "321321321", transfer_limit=200)
checkAcc2 = CheckingAccount("Michael Anderson", 600, 50, "321321", "123123123", transfer_limit=150)

checkAcc1.print_customer_information()
checkAcc1.deposit(100)
checkAcc1.withdraw(50)
checkAcc1.transfer(250, checkAcc2)
checkAcc1.transfer(150, checkAcc2)
checkAcc1.print_customer_information()
checkAcc2.print_customer_information()

#Scenario 2 - User opens savings account, deposits money, earns interest,
#then trys a withdrawal that bring the balance below the minimum balance

savings1 = SavingsAccount("Michelle Jhonson", 1000, 100, "123123", "321321321", interest_rate = 0.03)
savings2 = SavingsAccount("Michael Anderson", 2500, 200, "321321", "123123123", interest_rate = 0.015)

savings1.print_customer_information()
savings1.deposit(200)
savings1.apply_interest()
savings1.withdraw(2000)
savings1.print_customer_information()

savings2.print_customer_information()
savings2.apply_interest()
savings2.withdraw(500)
savings2.print_customer_information()




