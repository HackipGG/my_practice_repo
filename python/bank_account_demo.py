from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)
account1.deposit(1000)
print(account1)
account2 = BankAccount("1235", 52.1)
print(account2)
account2.withdraw(19.5)
print(account2)