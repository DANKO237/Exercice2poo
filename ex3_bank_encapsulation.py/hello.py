class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

   @property
   def balance(self):
     return self.__balance

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("Depot impossible")

    def withdraw(self, amount):
        if amount  0 and amount = self.balance:
            self.__balance -= amount
        else:
            print("Retrait impossible")

account = BankAccount("Alice", 1000)
print(account.balance)
print(account.deposit(500))
print(account.balance)
print(account.withdraw(300))
print(account.balance)
print(account.withdraw(5000))
print(account.balance)