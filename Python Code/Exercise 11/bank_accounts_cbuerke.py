"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 11.4 - Bank Accounts
Date: 11/18/2022

Description:
    Doesn't matter

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
class Account:
    def __init__(self, balance):
        self.balance = balance
        print(f"New account balance: ${balance}")


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: ${amount:0.2f}")
        return

    def withdraw(self, amount):
        print(f"Withdraw: ${amount:0.2f}")
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds. Withdrawal canceled.")
        return
    
    def get_balance(self):
        print(f"Balance: ${self.balance:0.2f}")
        return

class Savings(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest payment: ${interest:0.2f}")
        self.balance += interest
        return


def main():
    account = Savings(200, 10)
    account.deposit(12.34)
    account.get_balance()
    account.withdraw(40)
    account.get_balance()
    account.withdraw(200)
    account.get_balance()
    account.accrue_interest()
    account.accrue_interest()
    account.accrue_interest()
    account.withdraw(200)
    account.get_balance()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
