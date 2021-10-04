class BankAccount:
    allAccounts = []

    def __init__ (self, interestRate, balance):
        self.interestRate = interestRate
        self.balance = balance
        BankAccount.allAccounts.append(self)

    
    def deposit (self, amount):
        self.balance += amount
        return self

    
    def withdrawl (self, amount):
        if (self.balance - amount)>= 0:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: charging a $5 fee")
        return self

    
    def display_account_info(self):
        return f"{self.balance}"

    
    def yield_interest(self): #if balance is positive, it increases the account balance by the current balance*the interest rate
        if self.balance > 0:
            self.balance += (self.balance*self.interestRate)
        return self


    @classmethod
    def printallAccountsInfo(cls):
        for account in cls.allAccounts:
            account.display_account_info()



#Update the User class __init__ method	
class User:
    def __init__(self, firstName):
        self.firstName = firstName
        self.account = {
            "checkingAccount" : BankAccount(.03,2500),
            "retirementAccount" : BankAccount(.01,2000)
        }
# Update the User class make_deposit method (from BankAccount class)
# Update the User class make_withdrawal method (from BankAccount class)
# Update the User class display_user_balance method
    def display_user_balance(self): 
        print(f"User: {self.firstName}, Checking Balance: ${self.account['checkingAccount'].display_account_info()}")
        print(f"User: {self.firstName}, Retirement Balance: ${self.account['retirementAccount'].display_account_info()}")
        return self


    def transfer_money(self,amount,user):
        self.amount = self.amount - amount
        user.amount = user.amount + amount
        self.display_user_balance()
        user.display_user_balance()
        return self

User1 = User("User1")

User1.account['checkingAccount'].withdrawl(750)
User1.account['retirementAccount'].deposit(200)
User1.display_user_balance()



