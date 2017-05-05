# -*- coding: utf-8 -*-
"""
create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you'll create should have methods for each of the following:

Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account
"""

class BankAccount(object):
    balance=0
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "%s's accunt.Balance: ￥%.2f"%(self.name,self.balance)
    def show_balance(self):
        print "Balance: ￥%.2f"%(self.balance)
    def deposite(self,amount):
        if amount<=0:
            print "Nice try"
            return
        else:
            print "You are going to deposite ￥%.2f"%(amount)
            self.balance+=amount
            self.show_balance()

    def withdraw(self,amount):
        if amount<=0 or amount >self.balance:
            print "Don't kidding with me"
            return
        else:
            print "You are going to withdraw ￥%.2f"%(amount)
            self.balance-=amount
            self.show_balance()

my_account=BankAccount("Xiao")
print my_account
print my_account.show_balance()
my_account.deposite(2000)
my_account.withdraw(1000)
print my_account

        
